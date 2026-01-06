# Campus Connect Documentation

This folder contains project documentation and supplementary files that are not part of the Django application runtime.

## Contents

- `Campus_Connect_SRS_Complete_Document.docx` - Complete Software Requirements Specification
- `Campus_Connect_SRS_Complete_Document.htm` - HTML version of SRS
- `Campus_Connect_SRS_Complete_Document_files/` - Supporting files for HTML documentation
- Helper scripts for project setup and fixes

## Important Notes

- Files in this directory are **NOT** loaded by Django as templates or static assets
- This folder is isolated from the main application to prevent conflicts
- Documentation can be safely updated without affecting the running application
- All runtime code should remain in the main project directories (`blog/`, `users/`, `events/`, etc.)
