"""
RadioTrack - Department of Corrections Radio Management System
--------------------------------------
Models.py file for Streamlit UI
--------------------------------------
Author: Arthur Belanger (github.com/MusicalViking)
Copyright (c) 2025 Arthur Belanger
All rights reserved.
"""

import pandas as pd
from db_manager import DatabaseManager
import logging
import streamlit as st

logger = logging.getLogger(__name__)

# --------------------------------
# Item Management
# --------------------------------


def get_items(filters=None):
    """Get items from database with optional filters"""
    query = """
        SELECT id, category, name, location, condition, notes, created_date
        FROM items
        WHERE 1=1
    """
    params = []

    if filters:
        if "category" in filters and filters["category"]:
            query += " AND category = ?"
            params.append(filters["category"])
        if "location" in filters and filters["location"]:
            query += " AND location = ?"
            params.append(filters["location"])
        if "condition" in filters and filters["condition"]:
            query += " AND condition = ?"
            params.append(filters["condition"])
        if "search" in filters and filters["search"]:
            query += " AND (name LIKE ? OR notes LIKE ?)"
            search_term = f"%{filters['search']}%"
            params.extend([search_term, search_term])

    query += " ORDER BY created_date DESC"

    return DatabaseManager.execute_df_query(query, params)


def add_item(category, name, location, condition="Good", notes=""):
    """Add a new item to the database"""
    query = """
        INSERT INTO items (category, name, location, condition, notes, created_date)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """
    try:
        success = DatabaseManager.execute_query(
            query, (category, name, location, condition, notes), commit=True
        )
        if success:
            logger.info(f"Item added successfully: {name} ({category})")
        else:
            logger.error(f"Failed to add item: {name} ({category})")
        return success
    except Exception as e:
        logger.error(f"Error adding item: {e}")
        return False


def update_item(item_id, category, name, location, condition, notes):
    """Update an existing item"""
    query = """
        UPDATE items
        SET category = ?, name = ?, location = ?, condition = ?, notes = ?
        WHERE id = ?
    """
    try:
        success = DatabaseManager.execute_query(
            query, (category, name, location, condition, notes, item_id), commit=True
        )
        if success:
            logger.info(f"Item updated successfully: {name} (ID: {item_id})")
            return True
        else:
            logger.error(f"Failed to update item: {name} (ID: {item_id})")
            return False
    except Exception as e:
        logger.error(f"Error updating item {item_id}: {str(e)}")
        return False


def delete_item(item_id):
    """Delete an item by ID"""
    if not item_id:
        logger.error("No item ID provided for deletion")
        return False

    # First check if item exists
    check_query = "SELECT COUNT(*) FROM items WHERE id = ?"
    try:
        result = DatabaseManager.execute_query(check_query, (item_id,), fetch=True)
        if not result or result[0][0] == 0:
            logger.error(f"Item not found for deletion: ID {item_id}")
            return False
    except Exception as e:
        logger.error(f"Error checking item existence: {str(e)}")
        return False

    # Delete the item
    delete_query = "DELETE FROM items WHERE id = ?"
    try:
        success = DatabaseManager.execute_query(delete_query, (item_id,), commit=True)
        if success:
            logger.info(f"Item deleted successfully: ID {item_id}")
            return True
        else:
            logger.error(f"Failed to delete item: ID {item_id}")
            return False
    except Exception as e:
        logger.error(f"Error deleting item {item_id}: {str(e)}")
        return False


# --------------------------------
# Employee Management
# --------------------------------


def get_employees():
    """Get all employees"""
    query = """
        SELECT
            username, first_name, last_name, user_role as role,
            is_active, password_change_required
        FROM employees
        ORDER BY last_name, first_name
    """
    return DatabaseManager.execute_df_query(query)


def get_employee(username):
    """Get employee information by username"""
    query = """
        SELECT username, first_name, last_name, user_role, id
        FROM employees
        WHERE username = ?
    """
    result = DatabaseManager.execute_query(query, (username,), fetch=True)

    if result and result[0]:
        employee = result[0]
        return {
            "username": employee[0],
            "first_name": employee[1],
            "last_name": employee[2],
            "role": employee[3],
            "id": employee[4],
        }
    return None


def add_employee(
    first_name,
    last_name,
    position,
    email,
    phone,
    username,
    password,
    user_role="employee",
):
    """Add a new employee with specified role"""
    # Check if username already exists
    check_query = "SELECT username FROM employees WHERE username = ?"
    result = DatabaseManager.execute_query(check_query, (username,), fetch=True)

    if result and result[0]:
        return False, "Username already exists. Please choose a different username."

    # Validate password strength
    from auth import validate_password_strength, hash_password

    is_valid, message = validate_password_strength(password)
    if not is_valid:
        return False, message

    # Insert employee with password change required and approved status
    query = """
        INSERT INTO employees (
            first_name, last_name, position, email, phone,
            username, password, user_role, password_change_required, is_approved
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        success = DatabaseManager.execute_query(
            query,
            (
                first_name,
                last_name,
                position,
                email,
                phone,
                username,
                hash_password(password),
                user_role,
                1,
                1,
            ),  # Set password_change_required to 1 and is_approved to 1
            commit=True
        )
        if success:
            logger.info(f"New employee added: {username} ({first_name} {last_name})")
            return (
                True,
                f"Employee {first_name} {last_name} added successfully as {user_role}! They will be required to change their password on first login.",
            )
        else:
            logger.error(f"Failed to add employee: {username}")
            return False, "Failed to add employee to database"
    except Exception as e:
        logger.error(f"Error adding employee {username}: {str(e)}")
        return False, f"Database error: {str(e)}"


def update_employee(username, first_name, last_name, role):
    """Update employee information"""
    query = """
        UPDATE employees
        SET first_name = ?, last_name = ?, user_role = ?
        WHERE username = ?
    """
    try:
        success = DatabaseManager.execute_query(query, (first_name, last_name, role, username), commit=True)
        if success:
            logger.info(f"Employee updated successfully: {username}")
            return True
        else:
            logger.error(f"Failed to update employee: {username}")
            return False
    except Exception as e:
        logger.error(f"Error updating employee {username}: {str(e)}")
        return False


def update_employee_status(employee_id, is_active):
    """Update employee active status"""
    query = """
        UPDATE employees
        SET is_active = ?
        WHERE id = ?
    """
    try:
        success = DatabaseManager.execute_query(query, (is_active, employee_id), commit=True)
        if success:
            logger.info(f"Employee status updated successfully: ID {employee_id}, active: {is_active}")
            return True
        else:
            logger.error(f"Failed to update employee status: ID {employee_id}")
            return False
    except Exception as e:
        logger.error(f"Error updating employee status {employee_id}: {str(e)}")
        return False


# --------------------------------
# Post Management
# --------------------------------


def add_post(author_username, content):
    """Add a new post to the post box"""
    query = """
        INSERT INTO posts (author_username, content)
        VALUES (?, ?)
    """
    try:
        success = DatabaseManager.execute_query(query, (author_username, content), commit=True)
        if success:
            logger.info(f"New post added successfully by {author_username}")
            return True
        else:
            logger.error(f"Failed to add post by {author_username}")
            return False
    except Exception as e:
        logger.error(f"Error adding post by {author_username}: {str(e)}")
        return False


def get_posts():
    """Get all posts with author information"""
    query = """
        SELECT p.id, p.content, p.created_date, p.author_username,
               COALESCE(e.first_name, p.author_username) as first_name,
               COALESCE(e.last_name, '') as last_name
        FROM posts p
        LEFT JOIN employees e ON p.author_username = e.username
        ORDER BY p.created_date DESC
    """
    return DatabaseManager.execute_df_query(query)


def delete_post(post_id):
    """Delete a post (admin only)"""
    query = "DELETE FROM posts WHERE id = ?"
    try:
        success = DatabaseManager.execute_query(query, (post_id,), commit=True)
        if success:
            logger.info(f"Post deleted successfully: ID {post_id}")
            return True
        else:
            logger.error(f"Failed to delete post: ID {post_id}")
            return False
    except Exception as e:
        logger.error(f"Error deleting post {post_id}: {str(e)}")
        return False


# --------------------------------
# Location and Category Management
# --------------------------------


def get_locations():
    """Get all locations"""
    from config import LOCATIONS

    return LOCATIONS


def get_categories():
    """Get all categories"""
    from config import CATEGORIES

    return CATEGORIES
