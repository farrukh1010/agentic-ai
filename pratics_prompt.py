# Few-shot prompting is a technique in prompt engineering where a model is given a small number of examples (the "shots") to learn a specific task or pattern. These examples guide the model to generate desired outputs for new, similar inputs. It leverages the model's ability to generalize from limited data without requiring fine-tuning. This approach is useful for tasks like classification, translation, or text generation, where providing a few clear examples helps the model understand the context and produce accurate results. Few-shot prompting is efficient, flexible, and mimics how humans learn from examples.

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

user_input = input ("Enter input:")

# Define the few-shot prompt with examples
few_shot_prompt = f"""
1. Problem Statement
● Current Issue:
The AI workouts are often repetitive - deliver the same workout over and over, lack a
clear progression strategy (examples: heavier weights, more reps, etc) and do not
adjust sufficiently based on user feedback or past performance data.
● Proposed Enhancement: Improve the “prompt” specificity and progressiveness of
the AI-generated workout programs by incorporating data from the previous 2-3 weeks
of workouts and user feedback.
2. Goals & Objectives
1) Progressive Overload:
a) Each workout should build on previous sessions in a safe, incremental manner
(e.g., sets, reps, load, intensity).

2) Contextual Adaptation:
a) Incorporate user’s past 2-3 weeks of data (exercises performed, loads used, user
feedback on difficulty/soreness) to tailor the next session.

3) User Feedback Integration:
a) Dynamically adjust the workout plan based on direct user feedback (e.g., “too
easy” or “too hard” ratings).

4) Specificity in Prompts:
a) Provide the AI with more granular details (previous workout data, progression
rules, feedback records) so it can produce more targeted and detailed workouts.

5) Increased Variety:
a) Reduce redundancy by ensuring exercise rotations and variations are
automatically planned to avoid repeating the same core exercises within a short
timeframe.

6) Please edit the prompt so that workouts do not repeat and have a progression to
previous workouts. Each day should be full body workout with legs, chest, back, arms

and abs. Exercises should be diverse using push/pull variations and different exercises
every day. Exercises should not be repeated in the week and weekly programs should
be different. Exercises and results should build on each week.
7) Workout format:
Workouts should be a progressive style workout meaning that each workout builds on
the previous and is a full body workout targeting arms, legs, chest, back, shoulders and
abs.
8) Preferred daily format:
Mon - workout, Tue - workout, Wed - rest, Thu - workout, Fri - workout, Sat - workout,
Sat - Rest

If they request a workout every day then program the rest day on the Wed and Sun. If
they skip a day then use that as a rest day substitute. Rest day should be a walk and
prescribed stretches.
9) Using different exercises:
Exercises should not be repeated for 1 week. AI should read previous workout data for
updating level (sets, reps and weight) based on past feedback and programming the
right exercises to eliminate repetition. Each day the exercise should focus on a different
“sub body part” for that main body part. (ie for arms one day bicep and the other day
tricep.)

10) Length: Each workout should be based on onboarding questions for duration. The
prompt should know the desired workout length and use the below format to generate an
exercise.
30 min: 2 warmup, 2 sets of 6-8 of each body part for main and 2-3 stretches that focus
on muscles worked.
45 min: 2 warmup, 3 sets of 8-10 of each body part for main and 2-3 stretches that focus
on muscles worked.
60 AND 60+ min: 3 warmup, 3-4 sets of 8-10 of each body part for main and 4-5
stretches that focus on muscles worked.
11) Level: Each exercise should be selected based on desired workout expertise. This data
is in the new video table. The prompt should consider this when selecting exercises.
Beginner: Use only beginner exercises
Intermediate: Use beginner and intermediate exercises
Advanced: Use beginner, intermediate and advanced exercises (limit advanced)
12) Equipment: Use only equipment listed in onboarding. Limit bodyweight if other options
are given.

7. Success Metrics
1. Reduced Workout Repetition: Zero identical exercises used in a week’s sessions.
2. User Feedback Integration: Workouts should incorporate the user’s reported
feedback (e.g., “too easy,” “too hard,” etc.).

PREVIOUS NOTES:

4. Proposed Solution
Enhance the existing AI prompt and logic to include:
1. Detailed Historical Context (Last 2-3 Weeks):
○ A structured summary of the user’s workout history: exercises done,
sets/reps/weights used, difficulty ratings, soreness levels, and any personal
notes.
○ This summary should be injected into the AI prompt every time it generates a
new workout.
2. Progression Logic Module:
○ Define rules for incremental changes in volume, intensity, and exercise
complexity.
○ For example, if user completed “3 sets of 8 reps at 50 lbs” on a bench press,
the system might suggest “3 sets of 10 reps at 50 lbs” or “3 sets of 8 reps at
55 lbs” after a week, provided user feedback is positive.

3. User Feedback Integration:
○ Incorporate a user feedback loop:
■ If a user marks a workout or exercise as “too hard,” reduce the
load/volume next session or insert an alternative exercise.
■ If “too easy,” increase intensity or switch to a more advanced
variation.
4. Prompt Template & Instructions:
○ Restructure the AI prompt to include:
■ User Profile: Fitness level, goal, equipment, injuries, etc.
■ Workout History: Data from last 2-3 weeks (e.g., exercises, reps,
weights, difficulty ratings, any missed days).
■ Progression Criteria: Specific guidelines for incrementing
sets/reps/weight or rotating exercises.
■ Feedback to Implementation: Explicit instructions on how to use
the feedback loop (e.g., if rating < X, do Y).

5. Detailed Requirements
5.1 Input Data Requirements
1. Historical Data (Mandatory):

○ For each workout in the last 2-3 weeks:
■ Exercise name
■ Sets x Reps (or time if interval-based)
■ Load used (if applicable)
■ Feedback rating (e.g., RPE, difficulty rating)
■ Any notes (e.g., soreness, injuries)

2. User Profile (Existing):
○ Fitness goal
○ Equipment list
○ Available workout days per week
3. Prompt Parameters (New):
○ “No immediate repetition” threshold (e.g., do not repeat the exact same
exercise for 2 consecutive days).
○ Increment step (e.g., 5%–10% increase in load or rep count) depending on
user level and feedback.

5.2 Output Requirements
1. Workout Plan per Session:
○ Detailed list of exercises, sets, reps (or intervals), rest periods.
○ Specific load recommendations (optional but highly desirable for
intermediate/advanced users).
○ Clear instructions if user feedback indicates a need for modification (e.g., “If
user rates previous squat as too easy, increase load by 5 lbs”). *Maybe
initiate an AI chat to ask how they resolved it*
2. Progression Explanation (Optional but Recommended):
○ A brief note in the workout describing why the changes were made (e.g.,
“We added one more set of lunges because your last workout’s difficulty
rating was low”).
3. Exercise Variation Rotation:
○ Provide alternative exercises when repeating a movement pattern (e.g.,
barbell squats → goblet squats → split squats) to keep workouts fresh.

this is the user query and you have to response it and resposne should be in json formate
Sentence: {user_input}
Sentiment:"""

# Invoke the LLM with the few-shot prompt
result = llm.invoke(few_shot_prompt)

# Print the result
print(result)