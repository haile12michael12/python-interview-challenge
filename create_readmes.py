"""
Script to create README files for all challenge directories.
"""

import os

def create_readme_for_directory(dir_path, content):
    """Create a README.md file in the given directory if it doesn't exist."""
    readme_path = os.path.join(dir_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created README.md in {dir_path}")
    else:
        print(f"README.md already exists in {dir_path}")

def get_week1_content(day_name, challenge_name, advanced_twist):
    """Get content for week 1 README files."""
    return f"""# {day_name}: {challenge_name}

## Challenge
[Description of the {challenge_name.lower()} challenge]

## Advanced Twist
{advanced_twist}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week2_content(day_name, challenge_name, advanced_twist):
    """Get content for week 2 README files."""
    return f"""# {day_name}: {challenge_name}

## Challenge
[Description of the {challenge_name.lower()} challenge]

## Advanced Twist
{advanced_twist}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week3_content(day_name, challenge_name, advanced_twist):
    """Get content for week 3 README files."""
    return f"""# {day_name}: {challenge_name}

## Challenge
[Description of the {challenge_name.lower()} challenge]

## Advanced Twist
{advanced_twist}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week4_content(day_name, challenge_name, advanced_twist):
    """Get content for week 4 README files."""
    return f"""# {day_name}: {challenge_name}

## Challenge
[Description of the {challenge_name.lower()} challenge]

## Advanced Twist
{advanced_twist}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week5_content(day_name, challenge_name, what_it_tests):
    """Get content for week 5 README files."""
    # Remove special characters for compatibility
    clean_name = challenge_name.replace("🧩", "[Puzzle]").replace("⚙️", "[Gear]").replace("💾", "[Floppy]").replace("📬", "[Envelope]").replace("🧠", "[Brain]").replace("☁️", "[Cloud]").replace("📡", "[Satellite]").replace("🕵️", "[Detective]").replace("🔐", "[Lock]").replace("🚀", "[Rocket]")
    return f"""# {day_name}: {clean_name}

## Challenge
[Description of the {clean_name.lower()} challenge]

## What It Tests
{what_it_tests}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week6_content(day_name, challenge_name, what_it_tests):
    """Get content for week 6 README files."""
    # Remove special characters for compatibility
    clean_name = challenge_name.replace("🐳", "[Whale]").replace("🧱", "[Bricks]").replace("👁️", "[Eye]").replace("🔁", "[Repeat]").replace("🔒", "[Lock]").replace("☁️", "[Cloud]").replace("🌩️", "[CloudWithLightning]")
    return f"""# {day_name}: {clean_name}

## Challenge
[Description of the {clean_name.lower()} challenge]

## What It Tests
{what_it_tests}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week7_content(day_name, challenge_name, what_it_tests):
    """Get content for week 7 README files."""
    # Remove special characters for compatibility
    clean_name = challenge_name.replace("🤖", "[Robot]").replace("📝", "[Memo]").replace("👁️", "[Eye]").replace("🎮", "[Game]").replace("📈", "[Chart]").replace("🧠", "[Brain]").replace("📊", "[BarChart]")
    return f"""# {day_name}: {clean_name}

## Challenge
[Description of the {clean_name.lower()} challenge]

## What It Tests
{what_it_tests}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def get_week8_content(day_name, challenge_name, what_it_tests):
    """Get content for week 8 README files."""
    # Remove special characters for compatibility
    clean_name = challenge_name.replace("🏢", "[Office]").replace("🔄", "[Recycle]").replace("📈", "[Chart]").replace("🛡️", "[Shield]").replace("⚡", "[Lightning]").replace("🎯", "[Target]")
    return f"""# {day_name}: {clean_name}

## Challenge
[Description of the {clean_name.lower()} challenge]

## What It Tests
{what_it_tests}

## Requirements
- [List of requirements]

## Implementation Tips
- [Tips for implementation]

## Testing
- [Testing approach]
"""

def main():
    """Main function to create README files."""
    base_path = "python- challenge project"
    
    # Week 1 directories
    week1_dirs = [
        ("day01_lru_cache", "LRU Cache", "Add Redis-backed persistence"),
        ("day02_json_parser", "Custom JSON Parser", "Support nested objects + arrays"),
        ("day03_dependency_injection", "Dependency Injection Container", "Add decorators for autowiring"),
        ("day04_command_pattern", "Command Pattern Undo/Redo", "Use event sourcing to persist states"),
        ("day05_context_manager", "Context Manager", "Add async context support"),
        ("day06_testing_framework", "Unit Testing Framework", "Add parallel test execution"),
        ("day07_legacy_refactor", "Legacy Refactor", "Introduce SOLID and Type Hints refactor")
    ]
    
    for dir_name, challenge_name, advanced_twist in week1_dirs:
        dir_path = os.path.join(base_path, "week1_core_foundations", dir_name)
        if os.path.exists(dir_path):
            content = get_week1_content(dir_name, challenge_name, advanced_twist)
            create_readme_for_directory(dir_path, content)
    
    # Week 2 directories
    week2_dirs = [
        ("day08_async_crawler", "Async Web Crawler", "Add rate limiting and error retry logic"),
        ("day09_threadsafe_cache", "Thread-Safe Cache", "Benchmark vs Redis"),
        ("day10_producer_consumer", "Producer-Consumer System", "Add message prioritization"),
        ("day11_job_scheduler", "Async Job Scheduler", "Include cron-based job expressions"),
        ("day12_batch_runner", "Batch Runner", "Add backoff strategy and metrics"),
        ("day13_benchmark_io_cpu", "Benchmark CPU vs I/O", "Visualize results via matplotlib"),
        ("day14_parallel_compressor", "Parallel File Compressor", "Add checksum validation")
    ]
    
    for dir_name, challenge_name, advanced_twist in week2_dirs:
        dir_path = os.path.join(base_path, "week2_concurrency_async", dir_name)
        if os.path.exists(dir_path):
            content = get_week2_content(dir_name, challenge_name, advanced_twist)
            create_readme_for_directory(dir_path, content)
    
    # Week 3 directories
    week3_dirs = [
        ("day15_url_shortener", "URL Shortener", "Add analytics dashboard"),
        ("day16_auth_system", "Auth System", "Add OAuth2 + Refresh Tokens"),
        ("day17_microservices", "Microservices", "Implement gRPC between services"),
        ("day18_message_queue", "Message Queue", "Add persistent message replay"),
        ("day19_file_upload_async", "Async File Upload", "Use background tasks with Celery"),
        ("day20_rate_limiter", "Rate Limiter", "Add Redis and IP-based rules"),
        ("day21_cli_api_tool", "CLI API Client", "Support interactive mode")
    ]
    
    for dir_name, challenge_name, advanced_twist in week3_dirs:
        dir_path = os.path.join(base_path, "week3_backend_architecture", dir_name)
        if os.path.exists(dir_path):
            content = get_week3_content(dir_name, challenge_name, advanced_twist)
            create_readme_for_directory(dir_path, content)
    
    # Week 4 directories
    week4_dirs = [
        ("day22_log_analyzer", "Log Analyzer (10M Rows)", "Optimize with mmap + chunking"),
        ("day23_event_notification", "Event Notification", "Add WebSocket push"),
        ("day24_plugin_parser", "Plugin Parser", "Support live plugin hot-reload"),
        ("day25_stream_aggregator", "Stream Aggregator", "Simulate Kafka stream"),
        ("day26_mini_orm", "Mini ORM", "Add query caching layer"),
        ("day27_rule_engine", "Rule Engine", "Add dynamic rule persistence"),
        ("day28_observability_toolkit", "Observability Toolkit", "Export Prometheus metrics"),
        ("day29_monorepo_refactor", "Monorepo Refactor", "Add shared package + lint pipeline"),
        ("day30_distributed_analytics", "Distributed Analytics Platform", "Include API + Web Dashboard")
    ]
    
    for dir_name, challenge_name, advanced_twist in week4_dirs:
        dir_path = os.path.join(base_path, "week4_data_systems", dir_name)
        if os.path.exists(dir_path):
            content = get_week4_content(dir_name, challenge_name, advanced_twist)
            create_readme_for_directory(dir_path, content)
    
    # Week 5 directories
    week5_dirs = [
        ("day31_realtime_chat_server", "🧩 Realtime Chat Server (FastAPI + WebSockets)", "Concurrency, pub/sub, session handling"),
        ("day32_custom_task_queue", "⚙️ Custom Task Queue Engine (like Celery)", "Threading, job state persistence"),
        ("day33_in_memory_ts_database", "💾 In-Memory Time-Series Database", "Data structures, memory optimization"),
        ("day34_graphql_api_gateway", "📬 GraphQL API Gateway", "Schema stitching, query resolution"),
        ("day35_ml_api_wrapper", "🧠 Machine Learning API Wrapper", "Model serving + async inference"),
        ("day36_dockerized_deployment", "☁️ Dockerized Multi-Service Deployment", "DevOps + architecture"),
        ("day37_etl_pipeline", "📡 ETL Pipeline (Extract → Transform → Load)", "File streaming, data integrity"),
        ("day38_event_log_replay", "🕵️ Event Log Replay Simulator", "Replay system for debugging"),
        ("day39_access_control_middleware", "🔐 Access Control Middleware System (RBAC)", "Security, permissions, policy design"),
        ("day40_ai_analytics_cloud", "🚀 Final Capstone: AI-Driven Analytics Cloud", "Combine everything — full platform with API, tasks, and data pipelines")
    ]
    
    for dir_name, challenge_name, what_it_tests in week5_dirs:
        dir_path = os.path.join(base_path, "week5_advanced_bonus", dir_name)
        if os.path.exists(dir_path):
            content = get_week5_content(dir_name, challenge_name, what_it_tests)
            create_readme_for_directory(dir_path, content)
    
    # Week 6 directories
    week6_dirs = [
        ("day41_container_orchestration", "🐳 Container Orchestration (Kubernetes)", "Cluster management, scaling, health checks"),
        ("day42_infrastructure_as_code", "🧱 Infrastructure as Code (Terraform)", "Declarative infrastructure, state management"),
        ("day43_monitoring_logging", "👁️ Monitoring & Logging Stack", "Centralized logging, metrics collection"),
        ("day44_ci_cd_pipeline", "🔁 CI/CD Pipeline (GitHub Actions)", "Automated testing, deployment workflows"),
        ("day45_cloud_security", "🔒 Cloud Security Framework", "IAM, encryption, compliance scanning"),
        ("day46_serverless_architecture", "☁️ Serverless Architecture (AWS Lambda)", "Event-driven computing, cost optimization"),
        ("day47_multi_cloud_deployment", "🌩️ Multi-Cloud Deployment Strategy", "Vendor lock-in avoidance, redundancy")
    ]
    
    for dir_name, challenge_name, what_it_tests in week6_dirs:
        dir_path = os.path.join(base_path, "week6_cloud_devops", dir_name)
        if os.path.exists(dir_path):
            content = get_week6_content(dir_name, challenge_name, what_it_tests)
            create_readme_for_directory(dir_path, content)
    
    # Week 7 directories
    week7_dirs = [
        ("day48_ml_model_deployment", "🤖 ML Model Deployment Pipeline", "Model serving, versioning, A/B testing"),
        ("day49_nlp_processing_pipeline", "📝 NLP Processing Pipeline", "Text preprocessing, sentiment analysis"),
        ("day50_computer_vision_api", "👁️ Computer Vision API", "Image recognition, object detection"),
        ("day51_reinforcement_learning", "🎮 Reinforcement Learning Agent", "Decision making, reward optimization"),
        ("day52_time_series_forecasting", "📈 Time Series Forecasting System", "Predictive analytics, anomaly detection"),
        ("day53_auto_ml_pipeline", "🧠 AutoML Pipeline", "Automated feature engineering, hyperparameter tuning"),
        ("day54_model_monitoring", "📊 Model Monitoring & Drift Detection", "Performance tracking, data drift alerts")
    ]
    
    for dir_name, challenge_name, what_it_tests in week7_dirs:
        dir_path = os.path.join(base_path, "week7_ai_ml_engineering", dir_name)
        if os.path.exists(dir_path):
            content = get_week7_content(dir_name, challenge_name, what_it_tests)
            create_readme_for_directory(dir_path, content)
    
    # Week 8 directories
    week8_dirs = [
        ("day55_enterprise_microservices", "🏢 Enterprise Microservices Suite", "Distributed architecture, service mesh"),
        ("day56_distributed_data_pipeline", "🔄 Distributed Data Processing Pipeline", "Stream processing, fault tolerance"),
        ("day57_realtime_analytics_dashboard", "📈 Realtime Analytics Dashboard", "Live data visualization, interactive querying"),
        ("day58_security_incident_response", "🛡️ Security Incident Response System", "Threat detection, automated response"),
        ("day59_performance_optimization", "⚡ Performance Optimization Framework", "Profiling, caching, load testing"),
        ("day60_complete_system_architecture", "🎯 Complete System Architecture", "End-to-end solution, documentation, deployment")
    ]
    
    for dir_name, challenge_name, what_it_tests in week8_dirs:
        dir_path = os.path.join(base_path, "week8_final_capstone", dir_name)
        if os.path.exists(dir_path):
            content = get_week8_content(dir_name, challenge_name, what_it_tests)
            create_readme_for_directory(dir_path, content)

if __name__ == "__main__":
    main()