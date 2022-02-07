
# Hello world w Microsft Azure

Aplikacja "Hello world" z uzyciem srodowiska Azure Container Registry oraz Azure Kubernetes Service. Implementacja uslugi za pomoca Terraform oraz Dockera.




## Wymagania do uruchomienia

- Linux Ubuntu na naszej maszynie
- Git (instalacja wyjasniona ponizej)
- Terraform ([instrukcja instalacji](https://learn.hashicorp.com/tutorials/terraform/install-cli))
- Kubectl ([instrukcja instalacji](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/))
- Azure CLI ([instrukcja instalacji](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli))
- Docker (instalacja wyjasniona ponizej)


## Instalacja Dockera

Uruchom ponisze komendy, aby zainstalwoac Dockera:

```bash
  sudo su
```
```bash
  apt-get update
```
```bash
  apt-get install -qq apt-transport-https ca-certificates curl software-properties-common
```
```bash
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
```
```bash
  add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu '$(lsb_release -cs)' stable'
```
```bash
  apt-get update
```

```bash
  apt-get install -qq docker-ce
```

```bash
  sudo su
```

## Pobieranie repozytorium

Uruchom ponisze komendy, aby zainstalwoac Gita i pobrac repozytorium:

```bash
  sudo apt install git
```

```bash
  git clone https://github.com/rkasjan/kasapp.git
```

## Tworzenie obrazu w Dockerze

```bash
  cd kasapp
```

```bash
  docker build -t kasapp .
```

## Logowanie do Azure


```bash
  az login
```
Wchodzimy w wygenerowany link
```bash
  xdg-open: no method available for opening '
  https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=04b07795-8ddb-461a-bbee-02f9e1bf7b46&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A38443&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2F.default+offline_access+openid+profile&state=bxuoSAsJDfrjepgc&code_challenge=1IFtBV-j1x37WpO_YHIYD7RAulN7G4LGLcgJKdCcEsk&code_challenge_method=S256&nonce=eda14859a1dbd6bd72bf2cd29c94cef0d19b1d27b1c7de27378272f6f4636b6a&client_info=1&prompt=select_account'
```

## Uruchamianie i konfiguracja uslug (AKS & ACR) w Azure przez Terraform

```bash
  terraform init
```

```bash
  terraform plan
```
```bash
  terraform apply
```
```bash
  az acr login -n acrkas
```

```bash
  docker tag kasapp:latest acrkas.azurecr.io/kasapp:latest
```
```bash
  docker push acrkas.azurecr.io/kasapp
```
```bash
  az aks get-credentials --name aksKas --resource-group KasApp
```

## Start aplikacji

```bash
  az aks get-credentials --name aksKas --resource-group KasApp
```

```bash
  kubectl apply -f deployaks.yaml
```
```bash
  kubectl get all
```

W wyniku powyszej komendy otrzymamy adress IP dla serwisu "kasappsvc", ktory nalezy skopiowac

```bash
  NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kasappsvc    LoadBalancer   10.0.70.131   20.23.17.59   5000:30804/TCP   2m34s
service/kubernetes   ClusterIP      10.0.0.1      <none>        443/TCP          42m
```

```bash
curl 20.101.255.211:5000/hello/World
```

Otrzymamy nasze Hello World

```bash
<html>
<head>
<title>KasApp</title>
</head>
<body>
<center><strong>Hello World</strong></center>
</body>
</html>	
```
