CREATE DATABASE Electric_Vehicle_Population_Analysis;

CREATE TABLE Electric_Vehicle_Population_Data (
	`VIN (1-10)` VARCHAR(255),
	`County` VARCHAR(255),
	`City` VARCHAR(255),
	`State` VARCHAR(255),
	`Postal Code` VARCHAR(255),
	`Model Year` VARCHAR(255),
	`Make` VARCHAR(255),
	`Model` VARCHAR(255),
	`Electric Vehicle Type` VARCHAR(255),
	`Clean Alternative Fuel Vehicle (CAFV) Eligibility` VARCHAR(255),
	`Electric Range` VARCHAR(255),
	`Base MSRP` VARCHAR(255),
	`Legislative District` VARCHAR(255),
	`DOL Vehicle ID` VARCHAR(255),
	`Vehicle Location` VARCHAR(255),
	`Electric Utility` VARCHAR(255),
	`2020 Census Tract` VARCHAR(255)
);

-- Loading the Data
LOAD DATA LOCAL INFILE "C:/Users/nibed/Downloads/Electric_Vehicle_Population_Data.csv"
INTO TABLE Electric_Vehicle_Population_Data
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Let's view the entire Table
SELECT * FROM Electric_Vehicle_Population_Data;

-- Let's check the total records of our Dataset
SELECT COUNT(*)  
FROM Electric_Vehicle_Population_Data;

-- Let's get the details about the Dataset
DESCRIBE Electric_Vehicle_Population_Data;


-- Checking for missing values in specific columns
SELECT `Postal Code`
FROM Electric_Vehicle_Population_Data
ORDER BY `Postal Code`;

SELECT
  COUNT(*) AS total_rows,
  SUM(CASE WHEN `Postal Code` IS NULL OR TRIM(`Postal Code`) = '' 
			THEN 1 ELSE 0 END) AS postal_code_missing,
  SUM(CASE WHEN `Model Year` IS NULL OR TRIM(`Model Year`) = '' 
			THEN 1 ELSE 0 END) AS model_year_missing,
  SUM(CASE WHEN `Electric Range` IS NULL OR TRIM(`Electric Range`) = '' 
			THEN 1 ELSE 0 END) AS electric_range_missing,
  SUM(CASE WHEN `Base MSRP` IS NULL OR TRIM(`Base MSRP`) = '' 
			THEN 1 ELSE 0 END) AS msrp_missing,
  SUM(CASE WHEN `Legislative District` IS NULL OR TRIM(`Legislative District`) = '' 
			THEN 1 ELSE 0 END) AS district_missing,
  SUM(CASE WHEN `DOL Vehicle ID` IS NULL OR TRIM(`DOL Vehicle ID`) = '' 
			THEN 1 ELSE 0 END) AS dol_id_missing,
  SUM(CASE WHEN `2020 Census Tract` IS NULL OR TRIM(`2020 Census Tract`) = '' 
			THEN 1 ELSE 0 END) AS census_missing
FROM Electric_Vehicle_Population_Data;


-- Replacing All Blank Strings in Numeric Columns with NULL
UPDATE Electric_Vehicle_Population_Data
SET 
  `Postal Code` = NULLIF(TRIM(`Postal Code`), ''),
  `Model Year` = NULLIF(TRIM(`Model Year`), ''),
  `Electric Range` = NULLIF(TRIM(`Electric Range`), ''),
  `Base MSRP` = NULLIF(TRIM(`Base MSRP`), ''),
  `Legislative District` = NULLIF(TRIM(`Legislative District`), ''),
  `DOL Vehicle ID` = NULLIF(TRIM(`DOL Vehicle ID`), ''),
  `2020 Census Tract` = NULLIF(TRIM(`2020 Census Tract`), '');


-- Updating Data Types of the columns
ALTER TABLE Electric_Vehicle_Population_Data
	MODIFY COLUMN `Postal Code` VARCHAR(10),
	MODIFY COLUMN `Model Year` SMALLINT,
	MODIFY COLUMN `Electric Range` SMALLINT,
	MODIFY COLUMN `Base MSRP` INT,
	MODIFY COLUMN `Legislative District` SMALLINT,
	MODIFY COLUMN `DOL Vehicle ID` BIGINT,
	MODIFY COLUMN `2020 Census Tract` BIGINT;


# Data Exploration

-- Total Records & Distinct Counts
SELECT 
  COUNT(*) AS total_records,
  COUNT(DISTINCT `VIN (1-10)`) AS unique_vins,
  COUNT(DISTINCT `Make`) AS unique_makes,
  COUNT(DISTINCT `Model`) AS unique_models,
  COUNT(DISTINCT `Electric Vehicle Type`) AS unique_ev_types,
  COUNT(DISTINCT `Model Year`) AS unique_model_years
FROM Electric_Vehicle_Population_Data;


--  Top 10 Most Common EV Makes
SELECT `Make`, COUNT(*) count
FROM Electric_Vehicle_Population_Data
GROUP BY `Make`
ORDER BY count DESC
LIMIT 10;


-- Top 10 EV Models
SELECT `Model`, COUNT(*) count
FROM Electric_Vehicle_Population_Data
GROUP BY `Model`
ORDER BY count DESC
LIMIT 10;


-- Yearly Growth of EVs
SELECT `Model Year`, COUNT(*) count
FROM Electric_Vehicle_Population_Data
GROUP BY 1
ORDER BY 1 DESC;


-- EV Type Distribution
SELECT `Electric Vehicle Type`, COUNT(*) count
FROM Electric_Vehicle_Population_Data
GROUP BY 1;

/*
Washington State is witnessing a strong surge 
in BEV adoption, especially from 2024 onwards. 
With 80% of all EVs being fully electric and early 
registrations into 2026, the data reflects a bold 
step toward a zero-emission transportation future.
*/


-- Which Brands/Models are showing up for 2026?
SELECT `Model Year`, `Make`, `Model`, COUNT(*) count
FROM Electric_Vehicle_Population_Data
WHERE `Model Year` = 2026
GROUP BY `Make`, `Model`
ORDER BY count DESC;

/*
Interestingly, 1181 Tesla Model Y units 
are already registered as 2026 models — showing 
how EV market leaders are delivering future-ready 
vehicles well in advance. Alongside demo units from 
Cadillac and BMW, this emphasizes the early adoption 
and aggressive EV rollout strategy across manufacturers.
*/


-- Electric Range Over Time
SELECT `Model Year`, 
       AVG(`Electric Range`) avg_range, 
       COUNT(*) vehicle_count
FROM Electric_Vehicle_Population_Data
WHERE `Electric Range` IS NOT NULL
GROUP BY `Model Year`
ORDER BY `Model Year`;

SELECT `Model Year`, 
       AVG(`Electric Range`) avg_range, 
       COUNT(*) vehicle_count
FROM Electric_Vehicle_Population_Data
WHERE `Electric Range` IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;

-- Which make/year pairs are missing Electric Range?
SELECT `Model Year`, `Make`, 
		COUNT(*) vehicle_count, 
		AVG(`Electric Range`) avg_range
FROM Electric_Vehicle_Population_Data
WHERE `Electric Range` IS NOT NULL
GROUP BY 1, 2
ORDER BY 1 DESC, vehicle_count DESC;

/*
# TESLA & RIVIAN for 2025–2026 have range 
values completely missing or recorded as 0.0.

# These records exist — but range data 
wasn’t available at time of registration.

# These zeros are not real ranges — they’re 
basically placeholders (i.e., missing values).

# Including them in trend charts will skew 
our results and mislead viewers.
*/

SELECT `Model Year`, `Make`, 
		COUNT(*) vehicle_count, 
		AVG(`Electric Range`) avg_range
FROM Electric_Vehicle_Population_Data
WHERE `Electric Range` IS NOT NULL AND `Electric Range` > 0
GROUP BY 1, 2
ORDER BY 1 DESC, vehicle_count DESC;

/*
A significant portion of newer EV records 
(especially from Tesla and Rivian in 2025–2026) 
have electric range values marked as zero — likely 
due to early registrations or missing spec data 
at time of entry. These were excluded from 
average range analysis to avoid distortion.
*/




-- Top 10 Counties by EV Count
SELECT `County`, 
       COUNT(*) ev_count
FROM Electric_Vehicle_Population_Data
GROUP BY `County`
ORDER BY ev_count DESC
LIMIT 10;


-- Percent Share of Total
SELECT `County`, 
       COUNT(*) ev_count,
       ROUND(COUNT(`County`) * 100 / (SELECT COUNT(*) 
       FROM Electric_Vehicle_Population_Data), 2) AS percent_share
FROM Electric_Vehicle_Population_Data
GROUP BY `County`
ORDER BY ev_count DESC
LIMIT 10;

/*
King County dominates the EV landscape, accounting 
for nearly 50% of all electric vehicles, highlighting  
the strong EV culture in the Seattle metro region.
*/


-- County vs EV Type Split
SELECT `County`, 
		`Electric Vehicle Type`, 
		COUNT(*) count
FROM Electric_Vehicle_Population_Data
GROUP BY 1, 2
ORDER BY 1, count DESC;


-- CAFV Eligibility
ALTER TABLE Electric_Vehicle_Population_Data
CHANGE COLUMN `Clean Alternative Fuel Vehicle (CAFV) Eligibility` CAFV_Eligibility VARCHAR(255);

SELECT CAFV_Eligibility, 
       COUNT(*) AS count,
       ROUND(COUNT(CAFV_Eligibility) * 100 / (SELECT COUNT(*) 
       FROM Electric_Vehicle_Population_Data), 2) AS percent_eligibility
FROM Electric_Vehicle_Population_Data
GROUP BY CAFV_Eligibility
ORDER BY count DESC;

/*
Only 30% of registered EVs are confirmed to meet 
CAFV eligibility criteria, while over 60% remain 
unverified — a result of missing or unresearched 
battery range data, especially in newer models.
*/


# Base MSRP Analysis (EV Price Trends)

-- Clean Avg Price by Model Year
SELECT `Model Year`, 
       COUNT(*) vehicle_count,
       ROUND(AVG(`Base MSRP`), 2) avg_msrp,
       MIN(`Base MSRP`) min_msrp,
       MAX(`Base MSRP`) max_msrp
FROM Electric_Vehicle_Population_Data
WHERE `Base MSRP` IS NOT NULL AND `Base MSRP` > 0
GROUP BY 1
ORDER BY 1 DESC;

/*
Base MSRP data only exists for Model Years 2008–2020.

# What That Means?
For almost 90%+ of the records, Base MSRP is 
either missing or blank. So this column is:
	# Usable for limited historic pricing insight
	# Not usable for current market price analysis
    

MSRP data is available for earlier EV models (2008–2020) 
but largely missing for recent years, limiting price 
trend analysis. However, historic prices suggest 
EVs initially entered the market as premium vehicles, 
with some models priced over $80,000.

MSRP is a weak spot in the dataset and not worth visualizing 
further. Too many blanks, and it won't reflect today's market.
*/


# Let’s do a quick null value check so we know what we’re carrying forward.
SELECT 
  SUM(CASE WHEN `Electric Range` IS NULL OR `Electric Range` = 0 
			THEN 1 ELSE 0 END) AS missing_range,
  SUM(CASE WHEN `Base MSRP` IS NULL OR `Base MSRP` = 0 
			THEN 1 ELSE 0 END) AS missing_msrp,
  SUM(CASE WHEN CAFV_Eligibility IS NULL 
			THEN 1 ELSE 0 END) AS missing_cafv,
  SUM(CASE WHEN `Postal Code` IS NULL 
			THEN 1 ELSE 0 END) AS missing_postal,
  SUM(CASE WHEN `2020 Census Tract` IS NULL 
			THEN 1 ELSE 0 END) AS missing_census,
  SUM(CASE WHEN `Legislative District` IS NULL 
			THEN 1 ELSE 0 END) AS missing_legislative
FROM Electric_Vehicle_Population_Data;


-- Let's create a new table with cleaned data
CREATE TABLE EV_Cleaned AS
SELECT 
  `Model Year`,
  `Make`,
  `Model`,
  `Electric Vehicle Type`,
  `Electric Range`,
  CAFV_Eligibility,
  County,
  City,
  `Postal Code`,
  `Vehicle Location`,
  `Electric Utility`,
  `2020 Census Tract`,
  `Legislative District`
FROM Electric_Vehicle_Population_Data
WHERE `Electric Range` IS NOT NULL AND `Electric Range` > 0;

SELECT * FROM EV_Cleaned;

SELECT COUNT(*) FROM EV_Cleaned;

ALTER TABLE EV_Cleaned
	CHANGE COLUMN `Model Year` model_year SMALLINT,
	CHANGE COLUMN `Make` make VARCHAR(255),
	CHANGE COLUMN `Model` model VARCHAR(255),
	CHANGE COLUMN `Electric Vehicle Type` ev_type VARCHAR(255),
	CHANGE COLUMN `Electric Range` electric_range SMALLINT,
	CHANGE COLUMN CAFV_Eligibility cafv_eligibility VARCHAR(255),
	CHANGE COLUMN County county VARCHAR(255),
	CHANGE COLUMN City city VARCHAR(255),
	CHANGE COLUMN `Postal Code` postal_code VARCHAR(10),
	CHANGE COLUMN `Vehicle Location` vehicle_location VARCHAR(255),
	CHANGE COLUMN `Electric Utility` electric_utility VARCHAR(255),
	CHANGE COLUMN `2020 Census Tract` census_tract BIGINT,
	CHANGE COLUMN `Legislative District` legislative_district SMALLINT;

DESCRIBE EV_Cleaned;


SELECT * FROM ev_powerbi;

DESCRIBE ev_powerbi;

