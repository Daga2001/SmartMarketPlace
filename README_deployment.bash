# --------------------------------------------------------------------------------
# Este archivo es un atajo para ejecutar los comandos de kubernetes.
# --------------------------------------------------------------------------------

# namespace
kubectl create namespace smartmarketplace

# Start
kubectl apply -f  smp-app-deployments.yaml -n smartmarketplace
kubectl apply -f  smp-app-istio.yaml -n smartmarketplace
kubectl apply -f  smp-app-service.yaml -n smartmarketplace

# Start - 2.0
kubectl apply -f  smp-app-config.yaml -n smartmarketplace

# Delete
kubectl delete svc smp-app -n smartmarketplace
kubectl delete deployment smp-app -n smartmarketplace 
kubectl delete deployment smp-app-canary -n smartmarketplace

kubectl delete destinationrule smp-app -n smartmarketplace  
kubectl delete virtualservices smp-app -n smartmarketplace
kubectl delete gateway smp-app-gateway -n smartmarketplace

# Delete - 2.0

kubectl delete deployment smp-app-deployment -n smartmarketplace 
kubectl delete rc smp-app-deployment -n smartmarketplace 
kubectl delete svc smp-app-service -n smartmarketplace 

# Port-forwarding
kubectl port-forward svc/smp-app 80:80 -n smartmarketplace

# get all from smartmarketplace
kubectl get all -n smartmarketplace

# URL
http://34.28.89.171:30100

# API-url
http://localhost:8001/api/v1/namespaces/smartmarketplace/services/smp-app/proxy/ 