from pydantic import BaseModel
from typing import List, Optional


class UserQuestion(BaseModel):
    user_id: str
    question: str
    question_embedding: List[float]
    question_id: str
    answer: Optional[str] = ""
