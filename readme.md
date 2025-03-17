##### TESTE DE REDE
```
kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot -- /bin/bash
```

```
nc -zv
```

##### Remover todos os pods  do No e garantir que nenhum pod executara nele
```
k drain kind-worker --force  --ignore-daemonsets node/kind-worker 
```

##### Marcar no como nao escalavel mas nao remove pods.
```
k cordon kind-worker 
```

##### Fazer com que No possa voltar a operar.
```
k uncordon kind-worker
```