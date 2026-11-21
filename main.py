import random
import time

# Knowledge base for AI Concept Explainer & Quiz
topics_db = {
    "python": {
        "summary": "Python ek high-level, interpreted language hai jo clean syntax aur AI/Data Science ke liye use hoti hai.",
        "question": "Python mein loop ko turant rokne ke liye kaunsa keyword use hota hai?\n(a) stop\n(b) break\n(c) exit",
        "answer": "b"
    },
    "machine learning": {
        "summary": "Machine Learning AI ka ek hissa hai jisme system data se patterns seekh kar khud predictions karta hai.",
        "question": "Labeled data par train hone wale ML ko kya kehte hain?\n(a) Unsupervised Learning\n(b) Reinforcement Learning\n(c) Supervised Learning",
        "answer": "c"
    },
    "algorithm": {
        "summary": "Algorithm kisi bhi problem ko solve karne ke liye step-by-step instructions ka ek set hota hai.",
        "question": "Linear Search ki worst-case time complexity kya hoti hai?\n(a) O(n)\n(b) O(1)\n(c) O(log n)",
        "answer": "a"
    }
}

def generate_study_plan():
    print("\n--- AI SMART STUDY PLANNER ---")
    subject = input("Subject ka naam likhein (e.g., Python, Chemistry): ")
    days = int(input("Exam mein kitne din bache hain?: "))
    daily_hours = float(input("Roz kitne ghante padh sakte hain?: "))

    total_hours = days * daily_hours
    revision_days = max(1, days // 4)
    study_days = days - revision_days

    print(f"\n[AI Plan Generated for {subject}]")
    print(f"Total Study Time: {total_hours:.1f} ghante")
    print(f"1. Naye Topics Cover Karein: Pehle {study_days} din (Roz {daily_hours} ghante)")
    print(f"2. Mock Test & Revision: Aakhiri {revision_days} din")
    print("Tip: Har 45 minute baad 10 minute ka break zaroor lein.\n")

def run_quiz():
    print("\n--- AI CONCEPT EXPLAINER & QUIZ ---")
    score = 0
    for topic, data in topics_db.items():
        print(f"\nTopic: {topic.upper()}")
        print(f"Quick Note: {data['summary']}")
        print(f"\nQuestion: {data['question']}")
        user_ans = input("Apna answer likhein (a/b/c): ").strip().lower()
        
        if user_ans == data["answer"]:
            print("Sahi jawab!")
            score += 1
        else:
            print(f"Galat! Sahi jawab hai: ({data['answer']})")
            
    print(f"\nFinal Score: {score}/{len(topics_db)}")
    if score == len(topics_db):
        print("AI Feedback: Aapki taiyari solid hai!")
    else:
        print("AI Feedback: Jin topics mein galti hui, unhe ek baar phir revise karein.")

def main():
    while True:
        print("\n=========================================")
        print("   SMART AI STUDY & EXAM PREP ASSISTANT  ")
        print("=========================================")
        print("1. Generate Smart Study Plan")
        print("2. Take AI Concept Quiz")
        print("3. Exit")
        
        choice = input("\nOption chunein (1/2/3): ").strip()
        
        if choice == "1":
            generate_study_plan()
        elif choice == "2":
            run_quiz()
        elif choice == "3":
            print("All the best for your exams! Exiting...")
            break
        else:
            print("Invalid option! Kripya 1, 2, ya 3 chunein.")

if __name__ == "__main__":
    main()