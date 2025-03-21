from pydantic import BaseModel, Field, root_validator, ValidationError
from typing import Optional

class SalesSpreadsheet(BaseModel):
    Organizer: int = Field(..., description="Organizer identifier")
    Year_Month: str = Field(..., description="Year and month of the record")
    Day_of_Week: str = Field(..., description="Day of the week corresponding to the date")
    Day_Type: str = Field(..., description="Day classification: business day, holiday, etc.")
    Goal: str = Field(..., description="Campaign or action goal")
    Date: str = Field(..., description="Entry date in YYYY-MM-DD format")
    AdSet_name: Optional[str] = Field(None, description="Name of the ad set")
    Amount_spent: float = Field(0.0, ge=0, le=1200.00, description="Amount spent on the ad")
    Link_clicks: Optional[float] = Field(None, description="Number of link clicks", nullable=True)
    Impressions: Optional[float] = Field(0, description="Number of ad impressions", nullable=True)
    Conversions: Optional[float] = Field(None, description="Number of recorded conversions", nullable=True)
    Segmentation: Optional[str] = Field(None, description="Segmentation used in the ad")
    Ad_Type: str = Field(..., description="Type of ad")
    Phase: str = Field(..., description="Campaign phase")

    class Config:
        validate_default = True  # Ensures that default values are automatically validated



