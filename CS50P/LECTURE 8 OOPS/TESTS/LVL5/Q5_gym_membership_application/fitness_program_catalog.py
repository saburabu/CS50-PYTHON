class FitnessProgramCatalog:
    """Manages exercise programs and their associated activities as a list of dictionaries."""

    def __init__(self):
        self.programs = [
            {
                "program_name": "Weight Loss / Fat Loss",
                "activities": [
                    {
                        "name": "Brisk Treadmill Incline Walk",
                        "sets": 1,
                        "reps_or_duration": "30-45 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Kettlebell Swings",
                        "sets": 4,
                        "reps_or_duration": "15-20 reps",
                        "rest": "45s",
                    },
                    {
                        "name": "Burpees",
                        "sets": 3,
                        "reps_or_duration": "12-15 reps",
                        "rest": "60s",
                    },
                    {
                        "name": "Rowing Machine Intervals",
                        "sets": 8,
                        "reps_or_duration": "30s sprint / 30s rest",
                        "rest": "30s",
                    },
                ],
            },
            {
                "program_name": "Muscle Gain",
                "activities": [
                    {
                        "name": "Barbell Back Squat",
                        "sets": 4,
                        "reps_or_duration": "6-8 reps",
                        "rest": "120s",
                    },
                    {
                        "name": "Flat Barbell Bench Press",
                        "sets": 4,
                        "reps_or_duration": "6-8 reps",
                        "rest": "120s",
                    },
                    {
                        "name": "Pull-Ups (Weighted or Bodyweight)",
                        "sets": 3,
                        "reps_or_duration": "8-10 reps",
                        "rest": "90s",
                    },
                    {
                        "name": "Dumbbell Overhead Press",
                        "sets": 3,
                        "reps_or_duration": "8-12 reps",
                        "rest": "90s",
                    },
                ],
            },
            {
                "program_name": "Body Recomposition",
                "activities": [
                    {
                        "name": "Romanian Deadlift",
                        "sets": 4,
                        "reps_or_duration": "8-10 reps",
                        "rest": "90s",
                    },
                    {
                        "name": "Incline Dumbbell Press",
                        "sets": 3,
                        "reps_or_duration": "10-12 reps",
                        "rest": "75s",
                    },
                    {
                        "name": "Bulgarian Split Squats",
                        "sets": 3,
                        "reps_or_duration": "10 reps/leg",
                        "rest": "60s",
                    },
                    {
                        "name": "Assault Bike Finisher",
                        "sets": 5,
                        "reps_or_duration": "20s max / 40s easy",
                        "rest": "40s",
                    },
                ],
            },
            {
                "program_name": "Toning & Definition",
                "activities": [
                    {
                        "name": "Goblet Squats",
                        "sets": 3,
                        "reps_or_duration": "12-15 reps",
                        "rest": "60s",
                    },
                    {
                        "name": "Cable Face Pulls",
                        "sets": 3,
                        "reps_or_duration": "15 reps",
                        "rest": "45s",
                    },
                    {
                        "name": "Walking Lunges",
                        "sets": 3,
                        "reps_or_duration": "12 steps/leg",
                        "rest": "60s",
                    },
                    {
                        "name": "Push-Ups",
                        "sets": 3,
                        "reps_or_duration": "12-15 reps",
                        "rest": "45s",
                    },
                ],
            },
            {
                "program_name": "Facial Definition",
                "activities": [
                    {
                        "name": "Zone 2 Steady-State Cardio (Overall Fat Reduction)",
                        "sets": 1,
                        "reps_or_duration": "40 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Chin Tucks (Neck & Jaw Posture)",
                        "sets": 3,
                        "reps_or_duration": "15 reps",
                        "rest": "30s",
                    },
                    {
                        "name": "Neck Flexion & Extension Holds",
                        "sets": 3,
                        "reps_or_duration": "20s hold",
                        "rest": "30s",
                    },
                    {
                        "name": "Full-Body Circuit Training",
                        "sets": 3,
                        "reps_or_duration": "15 mins",
                        "rest": "60s",
                    },
                ],
            },
            {
                "program_name": "Healthy Weight Gain",
                "activities": [
                    {
                        "name": "Conventional Deadlift",
                        "sets": 3,
                        "reps_or_duration": "5-6 reps",
                        "rest": "150s",
                    },
                    {
                        "name": "Barbell Bent-Over Row",
                        "sets": 4,
                        "reps_or_duration": "8-10 reps",
                        "rest": "90s",
                    },
                    {
                        "name": "Leg Press",
                        "sets": 4,
                        "reps_or_duration": "10-12 reps",
                        "rest": "90s",
                    },
                    {
                        "name": "Parallel Bar Dips",
                        "sets": 3,
                        "reps_or_duration": "8-12 reps",
                        "rest": "90s",
                    },
                ],
            },
            {
                "program_name": "General Strength",
                "activities": [
                    {
                        "name": "Low-Bar Back Squat",
                        "sets": 5,
                        "reps_or_duration": "5 reps",
                        "rest": "180s",
                    },
                    {
                        "name": "Standing Overhead Barbell Press",
                        "sets": 5,
                        "reps_or_duration": "5 reps",
                        "rest": "150s",
                    },
                    {
                        "name": "Weighted Chin-Ups",
                        "sets": 4,
                        "reps_or_duration": "6 reps",
                        "rest": "120s",
                    },
                    {
                        "name": "Farmer's Carries",
                        "sets": 4,
                        "reps_or_duration": "40 meters",
                        "rest": "90s",
                    },
                ],
            },
            {
                "program_name": "Athletic Performance & Power",
                "activities": [
                    {
                        "name": "Box Jumps",
                        "sets": 4,
                        "reps_or_duration": "5 reps",
                        "rest": "90s",
                    },
                    {
                        "name": "Trap Bar Jumps",
                        "sets": 4,
                        "reps_or_duration": "4-6 reps",
                        "rest": "120s",
                    },
                    {
                        "name": "Medicine Ball Rotational Slams",
                        "sets": 3,
                        "reps_or_duration": "8 reps/side",
                        "rest": "60s",
                    },
                    {
                        "name": "20-Meter Sprints",
                        "sets": 6,
                        "reps_or_duration": "20m sprint",
                        "rest": "90s",
                    },
                ],
            },
            {
                "program_name": "Muscular Endurance",
                "activities": [
                    {
                        "name": "Bodyweight Squats",
                        "sets": 3,
                        "reps_or_duration": "25-30 reps",
                        "rest": "45s",
                    },
                    {
                        "name": "Dumbbell Thrusters (Light)",
                        "sets": 3,
                        "reps_or_duration": "20 reps",
                        "rest": "45s",
                    },
                    {
                        "name": "Battle Rope Waves",
                        "sets": 4,
                        "reps_or_duration": "45s continuous",
                        "rest": "30s",
                    },
                    {
                        "name": "Wall Sits",
                        "sets": 3,
                        "reps_or_duration": "60s hold",
                        "rest": "45s",
                    },
                ],
            },
            {
                "program_name": "Cardio & Stamina",
                "activities": [
                    {
                        "name": "Tempo Run",
                        "sets": 1,
                        "reps_or_duration": "30-45 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Jump Rope",
                        "sets": 5,
                        "reps_or_duration": "3 mins",
                        "rest": "60s",
                    },
                    {
                        "name": "Stair Climber",
                        "sets": 1,
                        "reps_or_duration": "25 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Cycling Threshold Intervals",
                        "sets": 4,
                        "reps_or_duration": "4 mins hard / 2 mins easy",
                        "rest": "120s",
                    },
                ],
            },
            {
                "program_name": "General Health & Longevity",
                "activities": [
                    {
                        "name": "Brisk Outdoor Walk",
                        "sets": 1,
                        "reps_or_duration": "30 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Kettlebell Deadlifts",
                        "sets": 3,
                        "reps_or_duration": "12 reps",
                        "rest": "60s",
                    },
                    {
                        "name": "Single-Leg Balance Stands",
                        "sets": 3,
                        "reps_or_duration": "30s/leg",
                        "rest": "30s",
                    },
                    {
                        "name": "Incline Push-Ups",
                        "sets": 3,
                        "reps_or_duration": "10-12 reps",
                        "rest": "60s",
                    },
                ],
            },
            {
                "program_name": "Stress Relief & Mental Health",
                "activities": [
                    {
                        "name": "Vinyasa Yoga Flow",
                        "sets": 1,
                        "reps_or_duration": "30 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Nature Jog or Walk",
                        "sets": 1,
                        "reps_or_duration": "30-45 mins",
                        "rest": "None",
                    },
                    {
                        "name": "Child's Pose with Deep Diaphragmatic Breathing",
                        "sets": 3,
                        "reps_or_duration": "60s hold",
                        "rest": "15s",
                    },
                    {
                        "name": "Light Shadowboxing",
                        "sets": 4,
                        "reps_or_duration": "2 mins",
                        "rest": "60s",
                    },
                ],
            },
            {
                "program_name": "Flexibility & Mobility",
                "activities": [
                    {
                        "name": "World's Greatest Stretch",
                        "sets": 3,
                        "reps_or_duration": "5 reps/side",
                        "rest": "30s",
                    },
                    {
                        "name": "90/90 Hip Switches",
                        "sets": 3,
                        "reps_or_duration": "10 reps",
                        "rest": "30s",
                    },
                    {
                        "name": "Thoracic Spine Open Books",
                        "sets": 3,
                        "reps_or_duration": "8 reps/side",
                        "rest": "30s",
                    },
                    {
                        "name": "Downward Dog to Cobra Flow",
                        "sets": 3,
                        "reps_or_duration": "8 slow reps",
                        "rest": "30s",
                    },
                ],
            },
            {
                "program_name": "Posture & Core Stability",
                "activities": [
                    {
                        "name": "Dead Bugs",
                        "sets": 3,
                        "reps_or_duration": "10 reps/side",
                        "rest": "45s",
                    },
                    {
                        "name": "Pallof Press",
                        "sets": 3,
                        "reps_or_duration": "12 reps/side",
                        "rest": "45s",
                    },
                    {
                        "name": "Bird-Dogs",
                        "sets": 3,
                        "reps_or_duration": "10 reps/side",
                        "rest": "30s",
                    },
                    {
                        "name": "Wall Angels",
                        "sets": 3,
                        "reps_or_duration": "12 reps",
                        "rest": "30s",
                    },
                ],
            },
            {
                "program_name": "Event or Milestone Prep",
                "activities": [
                    {
                        "name": "Full-Body Metabolic Circuit",
                        "sets": 4,
                        "reps_or_duration": "40s work / 20s rest",
                        "rest": "60s",
                    },
                    {
                        "name": "Dumbbell Thrusters",
                        "sets": 3,
                        "reps_or_duration": "12 reps",
                        "rest": "60s",
                    },
                    {
                        "name": "Plank Shoulder Taps",
                        "sets": 3,
                        "reps_or_duration": "20 taps",
                        "rest": "45s",
                    },
                    {
                        "name": "High-Incline Brisk Walk",
                        "sets": 1,
                        "reps_or_duration": "30 mins",
                        "rest": "None",
                    },
                ],
            },
        ]

    def get_all_programs(self) -> list[dict]:
        """Returns the complete list of program dictionaries."""
        return self.programs

    def get_program_by_name(self, name: str) -> dict | None:
        """Finds and returns a single program dictionary by name."""
        for program in self.programs:
            if program["program_name"].lower() == name.lower():
                return program
        return None

    def get_activities_name(self, program_name: str | None = None) -> list[str]:
        """Returns a list of activity names for a specific program, or all programs if None."""
        if program_name:
            program = self.get_program_by_name(program_name)
            if program:
                return [activity["name"] for activity in program["activities"]]
            return []

        return [
            activity["name"]
            for program in self.programs
            for activity in program["activities"]
        ]

    def add_activity(self, program_name: str, activity: dict) -> bool:
        """Appends a new activity dictionary to an existing program."""
        program = self.get_program_by_name(program_name)
        if program:
            program["activities"].append(activity)
            return True
        return False


if __name__ == "__main__":
    catalog = FitnessProgramCatalog()
    print("Total programs loaded:", len(catalog.get_all_programs()))
    print("Muscle Gain exercises:", catalog.get_activities_name("Muscle Gain"))
