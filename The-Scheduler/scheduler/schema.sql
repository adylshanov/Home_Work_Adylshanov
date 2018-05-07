
CREATE TABLE IF NOT EXISTS status (
  id_task INTEGER PRIMARY KEY AUTOINCREMENT,
  status_name TEXT
);

CREATE TABLE IF NOT EXISTS task (
	id_task	INTEGER PRIMARY KEY AUTOINCREMENT,
	name_task	TEXT NOT NULL DEFAULT '',
	test_task	TEXT NOT NULL DEFAULT '',
	date_create	DATE NOT NULL DEFAULT CURRENT_DATE,
	date_end	DATE,
	date_close	DATE,
	status_task	INTEGER DEFAULT 4,
  FOREIGN KEY(status_task) REFERENCES status_task(id_task)
);
