# FindIt — Smart Campus Lost and Found System

This version uses a modern, portfolio-inspired visual style based on the user's reference: dark navy hero, bold typography, blue accents, numbered sections, clean cards, and responsive layout.

## Files
- `app.py` — Flask backend and report/search/delete routes
- `templates/index.html` — responsive single-page UI
- `requirements.txt` — Python dependencies
- `Dockerfile` — container image instructions
- `deployment.yaml` — Kubernetes Deployment (2 replicas)
- `service.yaml` — Kubernetes NodePort Service

## Run locally (Windows)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000.

## Docker
Start Docker Desktop, then run in this folder:
```bash
docker build -t findit:v1 .
docker run --rm --name findit-app -p 5000:5000 findit:v1
```
Open http://localhost:5000.

## Kubernetes with Minikube
Prerequisites: Docker Desktop, Minikube, kubectl.
```bash
minikube start --driver=docker
minikube image build -t findit:v1 .
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get deployments
kubectl get pods
kubectl get services
minikube service findit-service
```

Scale to three replicas:
```bash
kubectl scale deployment findit-deployment --replicas=3
kubectl get pods
```

Logs and restart:
```bash
kubectl logs -l app=findit
kubectl rollout restart deployment/findit-deployment
kubectl rollout status deployment/findit-deployment
```

Clean up:
```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
minikube stop
```

## Notes
This student demo stores reports in memory. Data resets when the app restarts, and separate Kubernetes replicas do not share report data. A production-ready version should use a shared database such as PostgreSQL. Use demo contact information because contact details are displayed on the page.
