ALTER TABLE "event_event" ADD COLUMN  "frequency1" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "frequency2" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "frequency3" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "frequency4" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "interval1" integer;
ALTER TABLE "event_event" ADD COLUMN  "interval2" integer;
ALTER TABLE "event_event" ADD COLUMN  "interval3" integer;
ALTER TABLE "event_event" ADD COLUMN  "interval4" integer;
ALTER TABLE "event_event" ADD COLUMN  "by_monthday1" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_monthday2" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_monthday3" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_monthday4" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_month1" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_month2" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_month3" varchar(80);
ALTER TABLE "event_event" ADD COLUMN  "by_month4" varchar(80);


CREATE TABLE "event_event_by_day1" (
    "id" serial NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "days_id" integer NOT NULL REFERENCES "event_days" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("event_id", "days_id")
)
;

CREATE TABLE "event_event_by_day4" (
    "id" serial NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "days_id" integer NOT NULL REFERENCES "event_days" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("event_id", "days_id")
)
;
CREATE TABLE "event_event_by_day3" (
    "id" serial NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "days_id" integer NOT NULL REFERENCES "event_days" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("event_id", "days_id")
)
;
CREATE TABLE "event_event_by_day2" (
    "id" serial NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "days_id" integer NOT NULL REFERENCES "event_days" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("event_id", "days_id")
)
;