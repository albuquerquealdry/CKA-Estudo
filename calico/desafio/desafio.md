Cenário: Ambiente Seguro para uma Aplicação de Comércio Eletrônico
Você precisa configurar um ambiente para uma aplicação de comércio eletrônico, dividida em três serviços principais, cada um executado em diferentes namespaces no Kubernetes:

Frontend (namespace: frontend) - Responsável pela interface do usuário, acessível pelo cliente via HTTPS.
Backend (namespace: backend) - Fornece a lógica de negócios e expõe APIs internas para o frontend.
Banco de Dados (namespace: database) - Um banco de dados que armazena as informações dos produtos, pedidos e usuários.
O desafio é configurar políticas de rede Calico para controlar o tráfego e garantir a segurança e o isolamento entre esses componentes.

Requisitos de Políticas de Rede
Acesso ao Frontend:

Permitir que o frontend seja acessível a partir da Internet (simulada no cluster) somente via HTTP ou HTTPS na porta 80 ou 443.
Bloquear qualquer acesso externo ao backend e ao banco de dados.
Comunicação Interna entre Serviços:

O frontend deve se comunicar com o backend para enviar e receber dados via porta 8080.
O backend deve acessar o banco de dados no namespace database apenas na porta 5432.
Nenhum outro tráfego deve ser permitido entre esses namespaces.
Isolamento de Banco de Dados:

Somente o backend pode acessar o banco de dados. Qualquer tentativa de comunicação entre o frontend e o banco de dados deve ser bloqueada.
Acesso Administrativo ao Backend e ao Banco de Dados:

Apenas IPs internos da rede administrativa (por exemplo, 192.168.1.0/24) podem acessar o backend para fins de administração.
Nenhuma outra origem deve ter permissão para acessar diretamente esses serviços.
Implementação do Desafio
Namespace e Deployments: Crie namespaces e serviços de exemplo para cada parte da aplicação.

Configuração de Políticas com Calico:

Política para Acesso Externo: Defina uma política que permita o tráfego HTTP/HTTPS apenas para o frontend, bloqueando o backend e o banco de dados.
Política para Comunicação Interna: Crie uma política para permitir que o frontend acesse o backend, e outra para permitir que o backend se conecte ao banco de dados.
Isolamento de Banco de Dados: Especifique uma política para bloquear qualquer tentativa do frontend de acessar diretamente o banco de dados.
Acesso Administrativo: Crie uma política para permitir o acesso ao backend e banco de dados apenas de IPs da rede administrativa.
Testes:

Simule tentativas de conexão para validar que as políticas estão funcionando.
Teste acessos permitidos e bloqueados, verificando que cada serviço pode se comunicar apenas conforme especificado.