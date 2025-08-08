-- Drop existing tables if they exist
DROP TABLE IF EXISTS workflow_logs CASCADE;
DROP TABLE IF EXISTS workflows CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Table for storing user information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    totp_secret VARCHAR(255),
    role VARCHAR(50) DEFAULT 'user'
);

-- Table for storing workflow metadata
CREATE TABLE workflows (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_by INTEGER REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    trigger_type VARCHAR(100),
    trigger_value TEXT
);

-- Table for tasks belonging to a workflow
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    workflow_id INTEGER REFERENCES workflows(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_order INTEGER,
    output TEXT
);

-- Table for storing workflow execution logs
CREATE TABLE IF NOT EXISTS workflow_logs (
    id SERIAL PRIMARY KEY,
    workflow_id INTEGER REFERENCES workflows(id) ON DELETE CASCADE,
    executed_by INTEGER REFERENCES users(id),
    status VARCHAR(50),
    started_at TIMESTAMP,
    finished_at TIMESTAMP,
    log TEXT
);
