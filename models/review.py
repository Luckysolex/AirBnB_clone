#!/usr/bin/python3
"""Module containing the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class review inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
