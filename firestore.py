@firestore.transactional
def update_in_transaction(transaction, city_ref):
    snapshot = city_ref.get(transaction=transaction)
    new_population = snapshot.get(u'population') + 1

    if new_population < 1000000:
        transaction.update(city_ref, {u'population': new_population})
        return True
    else:
        return False
