-- 1. Insert Data into Admin Table
INSERT INTO "Admin" ("adminName", "password", "email")
VALUES
  ('Alice Admin', 'password123', 'alice.admin@example.com'),
  ('Bob Boss', 'securepass', 'bob.boss@example.com'),
  ('Charlie Chief', 'adminpass', 'charlie.chief@example.com');

-- 2. Insert Data into User Table
INSERT INTO "User" ("userName", "password", "email")
VALUES
  ('user_one', 'userpass1', 'user.one@example.com'),
  ('user_two', 'userpass2', 'user.two@example.com'),
  ('user_three', 'userpass3', 'user.three@example.com');

-- 3. Insert Data into Environment Table
INSERT INTO "Environment" ("environmentName")
VALUES
  ('Data Analysis Environment'),
  ('Machine Learning Environment'),
  ('Deep Learning Environment');

-- 4. Insert Data into Package Table
INSERT INTO "Package" ("packageName", "packageFilePath")
VALUES
  ('Numpy', '/path/to/numpy'),
  ('Pandas', '/path/to/pandas'),
  ('Scikit-Learn', '/path/to/scikit-learn'),
  ('TensorFlow', '/path/to/tensorflow'),
  ('Keras', '/path/to/keras');

-- 5. Insert Data into EnvironmentPackage Table
-- Ensure Environment and Package data are available before inserting here
INSERT INTO "EnvironmentPackage" ("environmentID", "packageID")
VALUES
  (1, 1), -- Data Analysis Environment includes Numpy
  (1, 2), -- Data Analysis Environment includes Pandas
  (2, 1), -- Machine Learning Environment includes Numpy
  (2, 2), -- Machine Learning Environment includes Pandas
  (2, 3), -- Machine Learning Environment includes Scikit-Learn
  (3, 1), -- Deep Learning Environment includes Numpy
  (3, 4), -- Deep Learning Environment includes TensorFlow
  (3, 5); -- Deep Learning Environment includes Keras

-- 6. Insert Data into Model Table
-- Ensure Admin, Environment, and User data are available before inserting here
INSERT INTO "Model" ("adminID", "environmentID", "userID", "ModelName", "category", "description", "documentation", "file_path")
VALUES
  (1, 1, 1, 'Sales Analysis Model', 'Data Analysis', 'Analyzes sales data.', 'Documentation for Sales Analysis Model', '/path/to/sales_analysis_model'),
  (2, 2, 2, 'Customer Segmentation Model', 'Machine Learning', 'Segments customers based on behavior.', 'Documentation for Customer Segmentation Model', '/path/to/customer_segmentation_model'),
  (3, 3, 3, 'Image Recognition Model', 'Deep Learning', 'Recognizes objects in images.', 'Documentation for Image Recognition Model', '/path/to/image_recognition_model');

-- 7. Insert Data into API Table
-- Ensure Model data is available before inserting here
INSERT INTO "API" ("modelID")
VALUES
  (1),
  (2),
  (3);

-- 8. Insert Data into Key Table
-- Ensure Admin and API data are available before inserting here
INSERT INTO "Key" ("adminID", "apiID", "key_value", "key_status")
VALUES
  (1, 1, 'key123', 'activated'),
  (2, 2, 'key456', 'deactivated'),
  (3, 3, 'key789', 'waiting');

-- 9. Insert Data into Feedback Table
-- Ensure User and Model data are available before inserting here
INSERT INTO "Feedback" ("userID", "modelID", "content")
VALUES
  (1, 1, 'Great model for sales analysis.'),
  (2, 2, 'The customer segmentation model is very useful.'),
  (3, 3, 'Impressive accuracy in image recognition.');

-- 10. Insert Data into Rating Table
-- Ensure User and Model data are available before inserting here
INSERT INTO "Rating" ("userID", "modelID", "stars")
VALUES
  (1, 1, 'five'),
  (2, 2, 'four'),
  (3, 3, 'five');

-- 11. Insert Data into Statistics Table
-- Ensure Model data is available before inserting here
INSERT INTO "Statistics" ("modelID", "stars_avg", "visits_count", "api_requests_count", "demo_usage_count", "comments_count")
VALUES
  (1, 5, 100, 50, 20, 10),
  (2, 4, 150, 60, 30, 15),
  (3, 5, 200, 70, 40, 20);

-- 12. Insert Data into Demo Table
-- Ensure Model data is available before inserting here
INSERT INTO "Demo" ("modelID", "demo_url")
VALUES
  (1, 'http://example.com/demo/sales_analysis'),
  (2, 'http://example.com/demo/customer_segmentation'),
  (3, 'http://example.com/demo/image_recognition');

-- 13. Insert Data into InputParameter Table
INSERT INTO "InputParameter" ("type", "parameterValue")
VALUES
  ('integer', '10'),
  ('string', 'sample input'),
  ('float', '0.5');

-- 14. Insert Data into ModelInputParameter Table
-- Ensure Model and InputParameter data are available before inserting here
INSERT INTO "ModelInputParameter" ("modelID", "inputParameterID")
VALUES
  (1, 1),
  (2, 2),
  (3, 3);
