from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Xiaohongshu(BaseModel):
    title: List[str] = Field(description="小紅書的5個標題", min_item=5, max_items=5)
    content: str = Field(description="小紅書的正文內容")