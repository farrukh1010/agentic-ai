
user_profile = """**User Profile & Onboarding Data**  
   - **Fitness Level:** [Beginner / Intermediate / Advanced]  
   - **Available Equipment:** [List: e.g., Barbells, Dumbbells, Resistance Bands, etc.]  
   - **Workout Frequency & Schedule:**  
     - Preferred Workout Days: Monday, Tuesday, Thursday, Friday, Saturday  
     - Rest Days: Wednesday and Sunday (if the user requests daily workouts, automatically schedule rest days on Wednesday and Sunday; if a workout is missed, consider that day as a rest day with light activity such as a walk and stretches)  
   - **Desired Workout Duration:** [30, 45, or 60+ minutes]  
     - *30 min:* 2 warmup exercises, 2 sets of 6-8 reps per main exercise, plus 2-3 stretches  
     - *45 min:* 2 warmup exercises, 3 sets of 8-10 reps per main exercise, plus 2-3 stretches  
     - *60+ min:* 3 warmup exercises, 3-4 sets of 8-10 reps per main exercise, plus 4-5 stretches  
"""

workout_history = """
**Workout History (Last 2-3 Weeks)**  
   - For each past workout session, include:  
     - **Exercise Name, Sets x Reps (or time), Load Used**  
     - **User Feedback:** e.g., "too easy," "just right," or "too hard"  
     - **Notes:** (e.g., soreness, injuries)  
   - Example history snippet:  
     - *Week 1, Monday:* Barbell Bench Press – 3x8 @ 50 lbs (Feedback: “too easy”)  
     - *Week 1, Tuesday:* Dumbbell Row – 3x8 @ 20 lbs (Feedback: “just right”)  
     - *Week 2, Monday:* Barbell Bench Press – 3x10 @ 50 lbs  
     - *Week 2, Tuesday:* Squats – 3x8 @ 60 lbs (Feedback: “challenging but manageable”)
     
"""

feedback = """
**Progression & Feedback Rules**  
   - **Progressive Overload:**  
     - Increase reps by 2 or load by approximately 5-10% if the previous workout feedback was “too easy.”  
     - If feedback was “just right” or “challenging but manageable,” maintain or slightly adjust the volume.  
     - If feedback was “too hard,” reduce the load/volume by approximately 10% or offer an easier exercise variation.
   - **Exercise Variation & Non-Repetition:**  
     - Each session must be a full-body workout targeting legs, chest, back, arms (alternating between biceps and triceps focus), shoulders, and abs.  
     - Do not repeat the exact same exercise (including sub-body part focus) within the same week.  
     - Rotate through alternative exercises for the same movement pattern (e.g., if Barbell Bench Press was used on one day, consider Dumbbell Bench Press or Incline Bench Press on another).
   - **Sub-Body Part Focus:**  
     - For arms, alternate between biceps and triceps focus each day.  
     - For legs and chest (and other major body parts), vary the sub-body part emphasis (e.g., for legs: alternate between quads and hamstrings).
   - **Video Table Data Utilization:**  
     - When selecting exercises, refer to the Videos table fields (workoutPhase, Equipment, BodyPart, subBodyPart, level).  
     - Only use exercises that match the user's available equipment and appropriate fitness level. For example, if the user is Intermediate, select from Beginner and Intermediate exercises (and limit advanced options).  
     - Ensure that if an exercise (by video ID or name) was used in a recent session (within the week), it is not repeated.

"""


workout_generation = """
 **Workout Generation Requirements**  
   - **Format:**  
     - Create a full-body workout plan that includes:  
       - Warmup: Appropriate number of exercises based on duration (2 or 3 exercises).  
       - Main Exercises: For each major body part (legs, chest, back, arms, shoulders, abs), list the exercise name, prescribed sets, reps, and load recommendations (if applicable).  
       - Cooldown/Stretches: Include 2-3 stretches for 30/45 minute sessions, or 4-5 stretches for 60+ minute sessions, focusing on muscles worked.
   - **Progression Explanation:**  
     - Add a brief note for any exercise modification explaining the progression rule applied (e.g., "Increased load due to previous feedback of 'too easy'").
   - **Safety & Adaptation:**  
     - If a user had any notes about soreness or injuries in recent sessions, include a cautionary note or suggest an alternative exercise that is less demanding.
   - **Dynamic Adjustments:**  
     - If a particular exercise was marked as “too hard” or “too easy,” adjust the next session accordingly as per the rules above.
"""

example_generation = """
**Example Instruction Segment for Today’s Workout Generation:**  

   
   Based on the user's profile and the past 2-3 weeks of workout data, generate today's full-body workout plan. Ensure that:
   - No exercise is repeated from earlier in the week.
   - Each exercise includes progression from the previous session (e.g., increased reps or load where feedback indicated “too easy”).
   - Exercises are selected using the Videos table data: match the user's equipment, body part, sub-body part, and level.
   - The plan includes warmups, main exercises for legs, chest, back, arms (alternating sub-body parts), shoulders, abs, and cooldown stretches.
   - The total workout duration is [30/45/60+] minutes.
   - Include a note explaining any progression decisions.
   - If any feedback indicated an exercise was “too hard,” replace that exercise with an easier alternative.
   """
   
final_output = """
6. **Final Output Requirements:**  
   - The generated workout must be detailed, including exercise names, sets x reps, load recommendations, and rest periods.  
   - It must provide variation from previous sessions and build on user performance and feedback.
   - Include a brief explanation of progression where applicable (e.g., “Increased bench press reps due to previous feedback indicating ease”).

"""


def workout_prompt(
    user_profile: str, workout_history: str, feedback: str, workout_generation: str, example_generation:str, final_output:str
) -> str:
    """this function generates a prompt for the nutritionist task"""
    return f"""
Become a professional gym trainer and perform tasks based on requirements given in triple backticks:


'''user_profile: {user_profile}'''
'''user_history: {workout_history}'''
'''user_progression_rules_and_feedback_example: {feedback}'''
'''workout_generation_requirements: {workout_generation}'''
'''Additional_rules: {example_generation}'''
'''Final_output_checklist: {final_output}'''

Format response as strictly JSON. Don't repeat the user given data.
Be precise and follow the instructions as much as possible. 

"""
