# Test Plan - Bug Report Generator

## 1. Overview
A test plan for the Bug Report Generator web application 
built with Python and Streamlit.

**Version:** 1.0  
**Date:** 2026-05-17  
**Tester:** Ilma Wafa  

## 2. Scope
Testing the Bug Report Generator web app for functional, 
edge case, and negative test scenarios.

## 3. Features to Test
- Form input validation
- Report generation
- Report formatting
- Download functionality

## 4. Test Cases

### TC001 - Empty Form Submission 
**Description:** Click Generate Report without filling any fields  
**Expected:** Warning message shown, report not generated  
**Actual:** TBD  
**Status:** Not tested

### TC002 — Spaces Only in Title
**Description:** Enter only spaces in the Bug Title field  
**Expected:** Warning shown, report not generated  
**Actual:** TBD  
**Status:** Not tested

### TC003 — Special Characters in Title
**Description:** Enter special characters like / \ ? * in title  
**Expected:** Report generates, filename handles special chars safely  
**Actual:** TBD  
**Status:** Not tested

### TC004 — Very Long Text Input
**Description:** Enter 1000+ characters in Steps to Reproduce  
**Expected:** App handles it without crashing  
**Actual:** TBD  
**Status:** Not tested