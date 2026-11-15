def search_users(users, search_text):
    lower_search = search_text.lower()
    return [
        user for user in users
        if lower_search in user["name"].lower()
        or lower_search in user["username"].lower()
        or lower_search in user["email"].lower()
    ]

def filter_users(users, search_text, city=None, company=None):
    results = search_users(users, search_text)
    filtered = []
    for user in results:
        city_match = city.lower() in user["address"]["city"].lower() if city else True
        company_match = company.lower() in user["company"]["name"].lower() if company else True
        if city_match and company_match:
            filtered.append(user)
    return filtered