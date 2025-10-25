# day41_container_orchestration: [Whale] Container Orchestration (Kubernetes)

## Challenge
Build a Kubernetes deployment configuration for a multi-service application with autoscaling, health checks, and rolling updates.

## What It Tests
Cluster management, scaling, health checks

## Requirements
- Create deployment YAML files for a web application with multiple services
- Implement health checks (liveness and readiness probes)
- Configure horizontal pod autoscaling based on CPU usage
- Set up rolling updates with zero downtime
- Implement resource limits and requests
- Configure service discovery and load balancing

## Implementation Tips
1. Use Kubernetes Deployments for managing replica sets
2. Implement proper liveness and readiness probes
3. Configure HorizontalPodAutoscaler based on CPU metrics
4. Use ConfigMaps and Secrets for configuration management
5. Set up proper resource limits to prevent resource contention
6. Implement proper labeling for service discovery

## Testing
Create test cases for:
- Deployment and scaling of pods
- Health check failures and recovery
- Rolling updates without downtime
- Resource limit enforcement
- Service connectivity between pods