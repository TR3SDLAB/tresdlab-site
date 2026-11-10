TR3S’D LAB — SITE COM PAINEL EDITÁVEL (Decap CMS)

IMPORTANTE: o painel não funciona só com arrastar a pasta para Netlify Drop.
Para salvar alterações, o site precisa estar conectado a um repositório GitHub e ter login OAuth configurado.

1. Crie um repositório GitHub (branch main) e envie TODOS os arquivos desta pasta para a raiz do repositório.
2. Edite admin/config.yml: troque USUARIO/REPOSITORIO pelo nome do seu repositório.
3. No Netlify, escolha Add new project > Import an existing project > GitHub; selecione o repositório. O build roda python3 scripts/build.py e publica a pasta raiz.
4. Configure autenticação GitHub OAuth para Decap CMS no Netlify, seguindo https://decapcms.org/docs/github-backend/ e https://docs.netlify.com/security/secure-access-to-sites/oauth-provider-tokens/ (as telas e disponibilidade podem mudar).
5. Acesse https://SEU-SITE.netlify.app/admin/ e entre com GitHub.
6. Em Produtos do catálogo, adicione/remova itens, suba fotos, altere preços, opções e ordem; publique. O GitHub dispara novo deploy automaticamente no Netlify.
7. Para fotos 360°, envie uma sequência ordenada de 24–36 imagens em Fotos 360°. Alternativamente, envie um modelo GLB em Modelo 3D interativo.
8. Em Configurações da loja > Contato, insira o WhatsApp com DDI 55, DDD e número, sem + ou espaços.

Não compartilhe senha ou tokens. O site público não deve conter chaves privadas.
A hospedagem gratuita depende dos limites e termos atuais do Netlify/GitHub.

TESTE LOCAL: python3 scripts/build.py e python3 -m http.server 8000; abra http://localhost:8000.
O painel /admin só permite salvar após autenticação e conexão ao repositório.
