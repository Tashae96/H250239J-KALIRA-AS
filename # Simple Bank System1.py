# Simple Bank System
# Demonstrates deposit, withdrawal, and balance check using loops and conditionals.

def main():
    balance = 0.0  # initial balance

    # Loop to keep the program running until the user chooses to exit
    while True:
        # Display menu options
        print("\n=== Simple Bank System ===") 
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        # Ask the user to choose an option
        choice = input("Enter your choice (1-4): ")

        # Option 1: Deposit money
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f" You have deposited ${amount:.2f}. New balance: ${balance:.2f}")
            else:
                print(" Oops! Invalid deposit amount.")

        # Option 2: Withdraw money
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Invalid withdrawal amount.")
            elif amount > balance:
                print("⚠️ Insufficient funds!")
            else:
                balance -= amount
                print(f" You withdrew ${amount:.2f}. Remaining balance: ${balance:.2f}")

        # Option 3: Check balance
        elif choice == '3':
            print(f" Your current balance is: ${balance:.2f}")

        # Option 4: Exit the program
        elif choice == '4':
            print(" Thank you for using the Simple Bank System!")
            break
        
        #invalid choice handling
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")
            
 # End of main function
if __name__ == "__main__":
    main()
