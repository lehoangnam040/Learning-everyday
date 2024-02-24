# General

## Functional requirement: 

- Upload:
  - client create a project, capture and store images in robot disk
  - client start upload images of a project from robot to server
  - client can upload images on same project on multiple robot, and be able to resolve conflict if other upload images before

- Download:
  - client can download a project with all images on other robot

## Non-functional requirement:
  - Integrity: all of bytes of an image must be uploaded and stored successfully on server
  - Availability: 
  - Rate Limit: should be implement if a client upload too many files at the same time

## Assumptions (min, avg, max)
- number of users = 50, 200, 500
- number project of each user = 1, 10, 30
- number of image / project = 10, 500, 10000
- image size = 1 MB, 20 MB, 100 MB
- many duplicate images using accross projects, duplicated percentage is about 20%

## Estimations
- total project = 500 * 30 = 15000
- total image = 15000 * 10000 = 150 millions
- project size = 10000 * 100 = 1 TB
- storage capacity: no duplicate = 15000 * 1TB = 15 PB
- storage capacity: optimized = 15 * (1 - 0.2) = 12 PB 

# Design

## High-Level Design


## Database Design


## Storage Design


# Requirements solving approachs