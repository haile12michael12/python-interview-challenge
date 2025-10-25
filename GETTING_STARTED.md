# Getting Started with Python Challenges

This guide will help you get started with both challenge collections in this repository.

## Repository Structure

```
python-interview-challenge/
├── README.md                           # Main repository overview
├── CHALLENGES_OVERVIEW.md              # Detailed comparison of both collections
├── GETTING_STARTED.md                  # This file
├── navigate_challenges.py              # Navigation helper script
│
├── python_challenges/                  # 100 Coding Challenges
│   ├── README.md
│   ├── CHALLENGES_SUMMARY.md
│   ├── intermediate/                   # 50 Intermediate Challenges
│   │   ├── README.md
│   │   ├── challenge_001.py
│   │   └── ... (50 total)
│   └── senior/                        # 50 Senior Challenges
│       ├── README.md
│       ├── challenge_001.py
│       └── ... (50 total)
│
└── python- challenge project/
    └── 30-Day-Senior-Python-Challenge/ # 60-Day Challenge
        ├── README.md
        ├── progress.md
        ├── requirements.txt
        ├── LICENSE
        ├── utils/
        ├── week1_core_foundations/     # Days 1-7
        ├── week2_concurrency_async/    # Days 8-14
        ├── week3_backend_architecture/ # Days 15-21
        ├── week4_data_systems/         # Days 22-30
        ├── week5_advanced_bonus/       # Days 31-40
        ├── week6_cloud_devops/         # Days 41-47
        ├── week7_ai_ml_engineering/    # Days 48-54
        └── week8_final_capstone/       # Days 55-60
```

## Choosing the Right Collection

### For Technical Interview Preparation:
- Use the **100 Coding Challenges** collection
- Start with **Intermediate** challenges if you're new to algorithms
- Progress to **Senior** challenges for advanced system design questions

### For Skill Development and Portfolio Building:
- Use the **60-Day Senior Python Challenge**
- Follow the structured curriculum week by week
- Build a portfolio of 60 projects showcasing different skills

## Getting Started with 100 Coding Challenges

1. **Navigate to the challenges directory:**
   ```bash
   cd python_challenges
   ```

2. **Choose your level:**
   - For intermediate developers: `cd intermediate`
   - For senior developers: `cd senior`

3. **Select a challenge:**
   - Start with lower numbered challenges
   - Read the problem description in the `.py` file
   - Implement your solution in the function template
   - Run the test cases at the bottom of the file

4. **Example workflow:**
   ```bash
   cd python_challenges/intermediate
   # Open challenge_001.py in your editor
   # Implement the solution
   python challenge_001.py  # Run tests
   ```

## Getting Started with 60-Day Challenge

1. **Install dependencies:**
   ```bash
   cd "python- challenge project/30-Day-Senior-Python-Challenge"
   pip install -r requirements.txt
   ```

2. **Follow the weekly structure:**
   - Start with Week 1 and progress sequentially
   - Each day builds on concepts from previous days
   - Use the `progress.md` file to track your completion

3. **Working on daily challenges:**
   ```bash
   cd week1_core_foundations/day01_lru_cache
   # Read the README.md for requirements
   # Implement your solution
   ```

## Progress Tracking

### For 100 Coding Challenges:
- Use the existing README files in each directory
- Manually track completed challenges
- Consider creating your own progress tracker

### For 60-Day Challenge:
- Use the `progress.md` file with checkboxes
- Update the file as you complete each day's challenge

## Recommended Learning Path

1. **Beginners:** Start with 100 Coding Challenges - Intermediate level
2. **Intermediate developers:** 
   - Complete 100 Coding Challenges - Senior level
   - Then start 60-Day Challenge
3. **Advanced developers:** Jump directly into 60-Day Challenge

## Tips for Success

1. **Set a consistent schedule:** Dedicate regular time each day
2. **Don't skip the theory:** Understand the underlying concepts
3. **Test thoroughly:** Use all provided test cases
4. **Review solutions:** Compare your approach with others
5. **Build a portfolio:** Document your solutions and learning

## Additional Resources

- Use `python navigate_challenges.py` for an interactive menu
- Refer to `CHALLENGES_OVERVIEW.md` for detailed information
- Check individual challenge README files for specific requirements