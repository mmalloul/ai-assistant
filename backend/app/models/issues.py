from pydantic import BaseModel, Field
from typing import List, Optional

class Issue(BaseModel):
    category: str = Field(description="The category of the issue ('Clean Code', 'Potential Bugs', 'Security Risks', 'Programming Principles').")
    location: str = Field(..., description="The location of the issue in the code, including file path and function name if applicable.")
    new_line_number: int = Field(..., description="The exact new line number of the issue in the code.")
    old_line_number: Optional[int] = Field(None, description="The exact old line number of the issue in the code, if applicable.")
    description: str = Field(..., description="A detailed description of the issue and why it is a problem. " +
                             "Provide context for the developer to understand the issue.")
    suggestion: str = Field(..., description="A suggested fix for the issue. Include a relevant code example in markdown format for easy copy-paste by the developer. " +
                            "Ensure the code example is concise and focused only on the issue identified, not the entire file.")

class ListOfIssues(BaseModel):
    issues: List[Issue] = Field(..., description="A list of potential issues identified in the code.")
