CREATE TYPE keyStatusValue AS ENUM (
  'activated',
  'deactivated',
  'waiting'
);

CREATE TYPE NumberOfStars AS ENUM (
  'one',
  'two',
  'three',
  'four',
  'five'
);
CREATE TABLE "Admin" (
  "adminID" serial PRIMARY KEY NOT NULL,
  "adminName" VARCHAR NOT NULL,
  "password" VARCHAR,
  "email" varchar UNIQUE NOT NULL,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "User" (
  "userID" serial PRIMARY KEY NOT NULL,
  "userName" VARCHAR UNIQUE NOT NULL,
  "password" VARCHAR NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);


CREATE TABLE "Model" (
  "modelID" serial PRIMARY KEY NOT NULL,
  "adminID" integer NOT NULL,
  "environmentID" integer NOT NULL,
  "userID" integer NOT NULL,
  "ModelName" VARCHAR NOT NULL,
  "category" VARCHAR NOT NULL,
  "uploaded_at" TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  "description" VARCHAR NOT NULL,
  "documentation" text NOT NULL,
  "file_path" varchar NOT NULL
);

CREATE TABLE "API" (
  "apiID" serial PRIMARY KEY NOT NULL,
  "modelID" integer NOT NULL
);

CREATE TABLE "Key" (
  "key_id" serial PRIMARY KEY NOT NULL,
  "adminID" integer NOT NULL,
  "apiID" integer NOT NULL,
  "key_value" varchar UNIQUE NOT NULL,
  "key_status" keyStatusValue NOT NULL
);

CREATE TABLE "Feedback" (
  "feedbackID" serial PRIMARY KEY NOT NULL,
  "userID" integer NOT NULL,
  "modelID" integer NOT NULL,
  "content" text NOT NULL,
  "provided_at" TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "Rating" (
  "ratingID" serial PRIMARY KEY NOT NULL,
  "userID" integer NOT NULL,
  "modelID" integer NOT NULL,
  "stars" NumberOfStars NOT NULL,
  "rated_at" TIMESTAMP NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "Statistics" (
  "stat_id" serial PRIMARY KEY NOT NULL,
  "modelID" integer NOT NULL,
  "stars_avg" integer DEFAULT 0,
  "visits_count" integer DEFAULT 0,
  "api_requests_count" integer DEFAULT 0,
  "demo_usage_count" integer DEFAULT 0,
  "comments_count" integer DEFAULT 0
);

CREATE TABLE "Demo" (
  "demoID" serial PRIMARY KEY NOT NULL,
  "modelID" integer NOT NULL,
  "demo_url" varchar NOT NULL
);

CREATE TABLE "Environment" (
  "environmentID" serial PRIMARY KEY NOT NULL,
  "environmentName" varchar NOT NULL
);

CREATE TABLE "Package" (
  "packageID" serial PRIMARY KEY NOT NULL,
  "packageName" varchar NOT NULL,
  "packageFilePath" varchar NOT NULL
);

CREATE TABLE "EnvironmentPackage" (
  "environmentID" integer NOT NULL,
  "packageID" integer NOT NULL,
  PRIMARY KEY ("environmentID", "packageID")
);

CREATE TABLE "InputParameter" (
  "inputParameterID" serial PRIMARY KEY NOT NULL,
  "type" varchar NOT NULL,
  "parameterValue" varchar NOT NULL
);

CREATE TABLE "ModelInputParameter" (
  "modelID" integer,
  "inputParameterID" integer,
  PRIMARY KEY ("modelID", "inputParameterID")
);

CREATE INDEX ON "Model" ("userID");

CREATE INDEX ON "Model" ("environmentID");

CREATE INDEX ON "API" ("modelID");

CREATE INDEX ON "Key" ("key_value");

CREATE INDEX ON "Key" ("apiID");

CREATE INDEX ON "Feedback" ("userID");

CREATE INDEX ON "Feedback" ("modelID");

CREATE INDEX ON "Rating" ("userID");

CREATE INDEX ON "Rating" ("modelID");

CREATE INDEX ON "Statistics" ("modelID");

CREATE INDEX ON "Demo" ("modelID");

ALTER TABLE "Model" ADD FOREIGN KEY ("adminID") REFERENCES "Admin" ("adminID");

ALTER TABLE "Model" ADD FOREIGN KEY ("environmentID") REFERENCES "Environment" ("environmentID");

ALTER TABLE "Model" ADD FOREIGN KEY ("userID") REFERENCES "User" ("userID");

ALTER TABLE "API" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "Key" ADD FOREIGN KEY ("adminID") REFERENCES "Admin" ("adminID");

ALTER TABLE "Key" ADD FOREIGN KEY ("apiID") REFERENCES "API" ("apiID");

ALTER TABLE "Feedback" ADD FOREIGN KEY ("userID") REFERENCES "User" ("userID");

ALTER TABLE "Feedback" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "Rating" ADD FOREIGN KEY ("userID") REFERENCES "User" ("userID");

ALTER TABLE "Rating" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "Statistics" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "Demo" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "EnvironmentPackage" ADD FOREIGN KEY ("environmentID") REFERENCES "Environment" ("environmentID");

ALTER TABLE "EnvironmentPackage" ADD FOREIGN KEY ("packageID") REFERENCES "Package" ("packageID");

ALTER TABLE "ModelInputParameter" ADD FOREIGN KEY ("modelID") REFERENCES "Model" ("modelID");

ALTER TABLE "ModelInputParameter" ADD FOREIGN KEY ("inputParameterID") REFERENCES "InputParameter" ("inputParameterID");

