#BankSample
def Bank(PlaceHolder,Branch,bal,name="SBI"):
    if bal<=1000:
        print(f"Hello {name} !! Your account balance is {bal} and your branch is {Branch} and your PlaceHolder is {PlaceHolder}")
        print("Your account balance is low. Please consider depositing more funds to avoid any inconvenience.")
    else:
        print(f"Hello {name} !! Your account balance is {bal} and your branch is {Branch} and your PlaceHolder is {PlaceHolder}")
        print("Your account balance is sufficient. Thank you for banking with us!")
Bank("Savings Account","Mumbai",500)
Bank("Current Account","Delhi",1500,"HDFC")
