"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI

app = FastAPI()
grading_log = []
completed = {}

# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
from grading import grade

@app.post("/grade")
def grade_ednpoint(data: dict):
    student = data["student"]
    lab = data["lab"]
    slow = data.get("slow", False)

    score = grade(student, lab, slow=slow)

    result = {"student": student, "lab": lab, "score": score}

    grading_log.append(result)

    return result 

# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
@app.get("/log")
def get_log():
    return {"entries": grading_log}

@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return {"statud": "cleared"}


# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
# Add a completed dict that maps submission IDs to results.
# Update POST /grade to check for an optional "submission_id" field —
# if the ID is already in completed, return the cached result without
# grading again or logging.
# Add POST /reset-completed endpoint.


# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
# TODO: job_submission_map = {}

# TODO: POST /grade-async endpoint

# TODO: run_grade_job helper function

# TODO: GET /grade-jobs/{job_id} endpoint