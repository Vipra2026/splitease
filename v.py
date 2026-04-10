members = []
expense_dic = []

def name():
    
    user_name = input("Enter name : ").lower()
    members.append(user_name)
    return members

def expense():
    activity_and_expense = {}
    paid_by = input("Who paid this : ").lower()

    user_activity = input("Enter activity : ")
    user_expense = int(input("Enter expense : "))
    activity_and_expense.update({user_activity:user_expense})

    print("All members included in this expense YES or NO ?")
    print("If YES enter y and if NO enter n.")

    user_choice = input("Enter y or n : ")

    while user_choice != "y" and user_choice != "n":
        print("Enter only y or n.")
        user_choice = input("Enter y or n : ")

    if user_choice == "y":
        involvement = members
        print("Go for the next move.")
    else:
        involved_members = input("Enter involved members : ").lower()
        involvement = involved_members.split(",")
    
    store_all = {

        "paid by" : paid_by,
        "expense details" : activity_and_expense,
        "involved members" : involvement
    }

    expense_dic.append(store_all)
    return expense_dic

def calculate_total():
    total = 0
    for val in expense_dic:
        amount = val["expense details"].values()
        for cal in amount:
            total+=cal
    return total

def calculate_settlements():
    total = 0
    share = {}
    if expense_dic == []:
        return []
    for val in expense_dic:
        amount = val["expense details"].values()
        for cal in amount:
            total = cal
        involved_members = val["involved members"]
        for member in involved_members:
            own_share = total/len(involved_members)
            if member in share:
                share[member] += own_share
            else:
                share.update({member : own_share})
    
    paid = {}
    balance = {}
    for v in expense_dic:
        paid_by = v["paid by"]
        amount = v["expense details"].values()
        for am in amount:
            paid_amount = am
        if paid_by in paid:
            paid[paid_by] += paid_amount
        else:
            paid.update({paid_by:paid_amount})
        
    for person in members:
        if person in paid and person in share:
            balance_amount = paid[person] - share[person]
        else:
            balance_amount = (-share[person])
        if person in balance:
            balance[person] += balance_amount
        else:
            balance.update({person:balance_amount})

    debtor_amounts = {}
    creditor_amounts = {}
    for p,q in balance.items():
        if q > 0:
            creditor_amounts.update({p:q})
        else:
            debtor_amounts.update({p:q})
    
    cred_sort = dict(sorted(creditor_amounts.items(), key=lambda item:item[1], reverse=True))
    debt_sort = dict(sorted(debtor_amounts.items(), key=lambda item:item[1]))
    
    settlements = []
    while debt_sort != {} and cred_sort != {}:
        debt_name, debt_amount = next(iter(debt_sort.items()))
        cred_name, cred_amount = next(iter(cred_sort.items()))

        payment = min(abs(debt_amount),cred_amount)
        pending_debt = abs(debt_amount) - payment
        pending_cred = cred_amount - payment

        debt_sort[debt_name] = pending_debt
        cred_sort[cred_name] = pending_cred

        settlements.append(f"{debt_name} pays {payment:.2f} to {cred_name}")
        
        if pending_debt == 0:
            del debt_sort[debt_name]
        if pending_cred == 0:
            del cred_sort[cred_name]

    return settlements
