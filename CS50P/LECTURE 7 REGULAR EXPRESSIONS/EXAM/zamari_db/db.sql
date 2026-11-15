-- MARKETPLACE DATABASE SETUP
-- WARNING: This resets the marketplace tables below and deletes their existing data.
-- It does NOT drop Supabase Auth users in auth.users.

create extension if not exists pgcrypto;

drop table if exists public.reviews cascade;
drop table if exists public.order_items cascade;
drop table if exists public.orders cascade;
drop table if exists public.cart_items cascade;
drop table if exists public.carts cascade;
drop table if exists public.products cascade;
drop table if exists public.stores cascade;
drop table if exists public.users cascade;

-- 1. USER PROFILES: one profile for each Supabase Auth user.
create table public.users (
    id uuid primary key references auth.users(id) on delete cascade on update cascade,
    full_name text not null,
    email text unique not null,
    phone text unique,
    avatar_url text,
    account_type text not null default 'customer'
        check (account_type in ('customer', 'seller', 'both')),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- 2. STORES
create table public.stores (
    id uuid primary key default gen_random_uuid(),
    owner_id uuid not null references public.users(id) on delete restrict on update cascade,
    name text not null,
    description text,
    logo_url text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- 3. PRODUCTS
create table public.products (
    id uuid primary key default gen_random_uuid(),
    store_id uuid not null references public.stores(id) on delete cascade on update cascade,
    name text not null,
    description text,
    category text,
    price numeric(12,2) not null check (price > 500),
    stock integer not null default 0 check (stock >= 0),
    image_url text,
    discount_percent numeric(5,2) not null default 0
        check (discount_percent between 0 and 100),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- 4. CARTS: one cart per customer.
create table public.carts (
    id uuid primary key default gen_random_uuid(),
    user_id uuid unique not null references public.users(id) on delete cascade on update cascade,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- 5. CART ITEMS
create table public.cart_items (
    id uuid primary key default gen_random_uuid(),
    cart_id uuid not null references public.carts(id) on delete cascade on update cascade,
    product_id uuid not null references public.products(id) on delete cascade on update cascade,
    product_name text not null,
    quantity integer not null default 1 check (quantity > 0),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    unique (cart_id, product_id)
);

-- 6. ORDERS
create table public.orders (
    id uuid primary key default gen_random_uuid(),
    customer_id uuid not null references public.users(id) on delete restrict on update cascade,
    order_number text unique not null,
    total_amount numeric(12,2) not null check (total_amount >= 0),
    status text not null default 'pending'
        check (status in ('pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled')),
    payment_status text not null default 'pending'
        check (payment_status in ('pending', 'paid', 'failed', 'refunded')),
    shipping_address text not null,
    shipping_phone text not null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- 7. ORDER ITEMS: snapshot product name and price at purchase time.
create table public.order_items (
    id uuid primary key default gen_random_uuid(),
    order_id uuid not null references public.orders(id) on delete cascade on update cascade,
    product_id uuid references public.products(id) on delete set null on update cascade,
    store_id uuid not null references public.stores(id) on delete restrict on update cascade,
    product_name text not null,
    quantity integer not null check (quantity > 0),
    unit_price numeric(12,2) not null check (unit_price >= 0),
    subtotal numeric(12,2) not null check (subtotal >= 0),
    created_at timestamptz not null default now()
);

-- 8. REVIEWS
create table public.reviews (
    id uuid primary key default gen_random_uuid(),
    customer_id uuid not null references public.users(id) on delete restrict on update cascade,
    product_id uuid references public.products(id) on delete set null on update cascade,
    order_item_id uuid unique references public.order_items(id) on delete set null on update cascade,
    rating integer not null check (rating between 1 and 5),
    comment text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- Keep updated_at current.
create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
    new.updated_at = now();
    return new;
end;
$$;

create trigger users_updated_at before update on public.users
for each row execute function public.set_updated_at();
create trigger stores_updated_at before update on public.stores
for each row execute function public.set_updated_at();
create trigger products_updated_at before update on public.products
for each row execute function public.set_updated_at();
create trigger carts_updated_at before update on public.carts
for each row execute function public.set_updated_at();
create trigger cart_items_updated_at before update on public.cart_items
for each row execute function public.set_updated_at();
create trigger orders_updated_at before update on public.orders
for each row execute function public.set_updated_at();
create trigger reviews_updated_at before update on public.reviews
for each row execute function public.set_updated_at();

-- Automatically create a public profile after Supabase Auth sign-up.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
    insert into public.users (id, full_name, email)
    values (
        new.id,
        coalesce(new.raw_user_meta_data ->> 'full_name', ''),
        new.email
    );
    return new;
end;
$$;

create trigger on_auth_user_created
after insert on auth.users
for each row execute function public.handle_new_user();

-- Fill profiles for Auth users that existed before this trigger was installed.
insert into public.users (id, full_name, email)
select
    id,
    coalesce(raw_user_meta_data ->> 'full_name', ''),
    email
from auth.users
where email is not null
on conflict (id) do nothing;

-- Useful indexes.
create index stores_owner_id_idx on public.stores(owner_id);
create index products_store_id_idx on public.products(store_id);
create index products_category_idx on public.products(category);
create index products_name_idx on public.products(name);
create index cart_items_cart_id_idx on public.cart_items(cart_id);
create index orders_customer_id_idx on public.orders(customer_id);
create index orders_status_idx on public.orders(status);
create index order_items_order_id_idx on public.order_items(order_id);
create index order_items_store_id_idx on public.order_items(store_id);
create index reviews_product_id_idx on public.reviews(product_id);

-- Enable Row Level Security on every application table.
alter table public.users enable row level security;
alter table public.stores enable row level security;
alter table public.products enable row level security;
alter table public.carts enable row level security;
alter table public.cart_items enable row level security;
alter table public.orders enable row level security;
alter table public.order_items enable row level security;
alter table public.reviews enable row level security;

-- USERS: a signed-in user can read/update only their own profile.
create policy "users_read_own"
on public.users for select to authenticated
using (id = (select auth.uid()));

create policy "users_update_own"
on public.users for update to authenticated
using (id = (select auth.uid()))
with check (id = (select auth.uid()));

-- STORES: public can browse; only the owner can manage their store.
create policy "stores_public_read"
on public.stores for select to anon, authenticated
using (true);

create policy "stores_owner_insert"
on public.stores for insert to authenticated
with check (
    owner_id = (select auth.uid())
    and exists (
        select 1 from public.users u
        where u.id = (select auth.uid())
          and u.account_type in ('seller', 'both')
    )
);

create policy "stores_owner_update"
on public.stores for update to authenticated
using (owner_id = (select auth.uid()))
with check (owner_id = (select auth.uid()));

create policy "stores_owner_delete"
on public.stores for delete to authenticated
using (owner_id = (select auth.uid()));

-- PRODUCTS: public can browse; store owners can manage their products.
create policy "products_public_read"
on public.products for select to anon, authenticated
using (true);

create policy "products_owner_insert"
on public.products for insert to authenticated
with check (
    exists (
        select 1 from public.stores s
        where s.id = store_id and s.owner_id = (select auth.uid())
    )
);

create policy "products_owner_update"
on public.products for update to authenticated
using (
    exists (
        select 1 from public.stores s
        where s.id = store_id and s.owner_id = (select auth.uid())
    )
)
with check (
    exists (
        select 1 from public.stores s
        where s.id = store_id and s.owner_id = (select auth.uid())
    )
);

create policy "products_owner_delete"
on public.products for delete to authenticated
using (
    exists (
        select 1 from public.stores s
        where s.id = store_id and s.owner_id = (select auth.uid())
    )
);

-- CARTS: customers can manage only their own cart.
create policy "carts_own_all"
on public.carts for all to authenticated
using (user_id = (select auth.uid()))
with check (user_id = (select auth.uid()));

-- CART ITEMS: access only through a cart owned by the signed-in user.
create policy "cart_items_own_all"
on public.cart_items for all to authenticated
using (
    exists (
        select 1 from public.carts c
        where c.id = cart_id and c.user_id = (select auth.uid())
    )
)
with check (
    exists (
        select 1 from public.carts c
        where c.id = cart_id and c.user_id = (select auth.uid())
    )
);

-- ORDERS: customers can read and create their own orders.
create policy "orders_own_read"
on public.orders for select to authenticated
using (customer_id = (select auth.uid()));

create policy "orders_own_insert"
on public.orders for insert to authenticated
with check (customer_id = (select auth.uid()));

-- Deliberately no general order update/delete policy for a desktop client.
-- Status/payment changes should be handled by trusted server-side logic later.

-- ORDER ITEMS: customer can read items in their order; store owner can read their store's items.
create policy "order_items_read_customer_or_store_owner"
on public.order_items for select to authenticated
using (
    exists (
        select 1 from public.orders o
        where o.id = order_id and o.customer_id = (select auth.uid())
    )
    or exists (
        select 1 from public.stores s
        where s.id = store_id and s.owner_id = (select auth.uid())
    )
);

create policy "order_items_insert_own_order"
on public.order_items for insert to authenticated
with check (
    exists (
        select 1 from public.orders o
        where o.id = order_id and o.customer_id = (select auth.uid())
    )
    and product_id is not null
    and exists (
        select 1 from public.products p
        where p.id = product_id and p.store_id = order_items.store_id
    )
);

-- REVIEWS: everyone can read; signed-in users manage their own.
create policy "reviews_public_read"
on public.reviews for select to anon, authenticated
using (true);

create policy "reviews_own_insert"
on public.reviews for insert to authenticated
with check (customer_id = (select auth.uid()));

create policy "reviews_own_update"
on public.reviews for update to authenticated
using (customer_id = (select auth.uid()))
with check (customer_id = (select auth.uid()));

create policy "reviews_own_delete"
on public.reviews for delete to authenticated
using (customer_id = (select auth.uid()));

-- API privileges. RLS still decides which rows a user may access.
grant usage on schema public to anon, authenticated;
grant select on public.stores, public.products, public.reviews to anon, authenticated;
grant select, update on public.users to authenticated;
grant insert, update, delete on public.stores, public.products to authenticated;
grant select, insert, update, delete on public.carts, public.cart_items to authenticated;
grant select, insert on public.orders to authenticated;
grant select, insert on public.order_items to authenticated;
grant insert, update, delete on public.reviews to authenticated;

-- Limit profile updates to ordinary profile fields; users cannot change their own email/id here.
revoke update on public.users from authenticated;
grant update (full_name, phone, avatar_url) on public.users to authenticated;
