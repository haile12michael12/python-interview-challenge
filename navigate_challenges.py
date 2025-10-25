"""
Script to help navigate the Python challenges in this repository.
"""

import os
import sys

def show_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("PYTHON CHALLENGES NAVIGATION")
    print("="*60)
    print("1. 100 Coding Challenges for Technical Interviews")
    print("   - 50 Intermediate Challenges")
    print("   - 50 Senior Challenges")
    print("\n2. 40-Day Senior Python Challenge")
    print("   - 5 Weeks of Intensive Learning")
    print("   - Project-Based Curriculum")
    print("\n3. Exit")
    print("="*60)

def show_coding_challenges_menu():
    """Display options for the coding challenges."""
    print("\n" + "-"*50)
    print("100 CODING CHALLENGES")
    print("-"*50)
    print("1. Intermediate Challenges (50)")
    print("2. Senior Challenges (50)")
    print("3. Back to Main Menu")
    print("-"*50)

def show_40_day_challenge_menu():
    """Display options for the 40-day challenge."""
    print("\n" + "-"*50)
    print("40-DAY SENIOR PYTHON CHALLENGE")
    print("-"*50)
    print("1. Week 1: Core Architecture (Days 1-7)")
    print("2. Week 2: Concurrency & Async (Days 8-14)")
    print("3. Week 3: Backend Systems (Days 15-21)")
    print("4. Week 4: Data & Analytics (Days 22-30)")
    print("5. Week 5: Advanced Projects (Days 31-40)")
    print("6. Back to Main Menu")
    print("-"*50)

def list_intermediate_challenges():
    """List all intermediate challenges."""
    challenges_dir = os.path.join("python_challenges", "intermediate")
    if os.path.exists(challenges_dir):
        print("\n" + "-"*50)
        print("INTERMEDIATE CHALLENGES")
        print("-"*50)
        challenges = [f for f in os.listdir(challenges_dir) if f.startswith("challenge_") and f.endswith(".py")]
        challenges.sort()
        for i, challenge in enumerate(challenges, 1):
            print(f"{i:2d}. {challenge}")
        print("-"*50)
    else:
        print("Intermediate challenges directory not found.")

def list_senior_challenges():
    """List all senior challenges."""
    challenges_dir = os.path.join("python_challenges", "senior")
    if os.path.exists(challenges_dir):
        print("\n" + "-"*50)
        print("SENIOR CHALLENGES")
        print("-"*50)
        challenges = [f for f in os.listdir(challenges_dir) if f.startswith("challenge_") and f.endswith(".py")]
        challenges.sort()
        for i, challenge in enumerate(challenges, 1):
            print(f"{i:2d}. {challenge}")
        print("-"*50)
    else:
        print("Senior challenges directory not found.")

def list_week_challenges(week_num):
    """List challenges for a specific week of the 40-day challenge."""
    week_dirs = {
        1: "week1_core_foundations",
        2: "week2_concurrency_async",
        3: "week3_backend_architecture",
        4: "week4_data_systems",
        5: "week5_advanced_bonus"
    }
    
    if week_num in week_dirs:
        week_dir = os.path.join("python- challenge project", "30-Day-Senior-Python-Challenge", week_dirs[week_num])
        if os.path.exists(week_dir):
            print(f"\n" + "-"*50)
            print(f"WEEK {week_num} CHALLENGES")
            print("-"*50)
            challenges = [d for d in os.listdir(week_dir) if os.path.isdir(os.path.join(week_dir, d))]
            challenges.sort()
            for i, challenge in enumerate(challenges, 1):
                print(f"{i:2d}. {challenge}")
            print("-"*50)
        else:
            print(f"Week {week_num} directory not found.")
    else:
        print("Invalid week number.")

def main():
    """Main navigation function."""
    while True:
        show_main_menu()
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            # 100 Coding Challenges
            while True:
                show_coding_challenges_menu()
                sub_choice = input("\nEnter your choice (1-3): ").strip()
                
                if sub_choice == "1":
                    list_intermediate_challenges()
                elif sub_choice == "2":
                    list_senior_challenges()
                elif sub_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            # 40-Day Challenge
            while True:
                show_40_day_challenge_menu()
                sub_choice = input("\nEnter your choice (1-6): ").strip()
                
                if sub_choice in ["1", "2", "3", "4", "5"]:
                    week_num = int(sub_choice)
                    list_week_challenges(week_num)
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "3":
            print("Thank you for using the Python Challenges repository!")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()