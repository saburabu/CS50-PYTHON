class Transaction:

  def __init__(self, transaction_id: int, description: str, amount: float):
    # lets blindly trust users input
    self.id = transaction_id
    self.description = description
    self.amount = amount


class TransactionCollection:

  def __init__(self):
    self.transactions = {}

  def save_transactions(self, transaction):
    if not isinstance(transaction, Transaction):
      raise ValueError("Your Transaction must be from the Transaction object")

    if transaction.id in self.transactions:
      raise ValueError("hafa no duplicate transfers for here guy")

    self.transactions[transaction.id] = transaction

  def __getitem__(self, key):
    if not isinstance(key, int) or isinstance(key, bool):
      raise ValueError("HAFA KEY MUST BE AN INT")

    if key not in self.transactions:
      raise KeyError("Key doesnt exist")

    return self.transactions[key]

  def __setitem__(self, key, value):
    if not isinstance(key, int) or isinstance(key, bool):
      raise ValueError("HAFA KEY MUST BE AN INT")

    if not isinstance(value, Transaction):
      raise ValueError("Value must be a Transaction object")

    if value.id != key:
      raise ValueError("Key must match transaction ID")

    self.transactions[key] = value

  def __len__(self):
    return len(self.transactions)

  def __contains__(self, item):
    if isinstance(item, Transaction):
      return item in self.transactions.values()
    return item in self.transactions
