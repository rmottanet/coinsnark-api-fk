# Coin Snark API

## ctrl+s :v:

Este projeto apresenta a API do Coin Snark, um serviço de conversão de moeda escrito em Python Flask. Ele oferece aos usuários uma maneira fácil de converter valores monetários entre diferentes moedas. A API faz parte de um projeto maior, que também inclui uma página frontend hospedada no GitHub Pages para fácil acesso às suas funcionalidades.

Embora este README ofereça uma visão geral breve, para uma compreensão abrangente, consulte a [documentação completa](https://rmottanet.gitbook.io/coinsnark).

## Recursos

- Fornece uma lista de moedas suportadas.
- Permite a conversão de moeda entre vários pares de moedas.
- API leve e fácil de usar para integração perfeita em aplicativos.

## Uso

Para usar a API do Coin Snark, os desenvolvedores precisam enviar solicitações HTTP para os endpoints designados. A API responde com dados JSON contendo as informações solicitadas ou os valores de moeda convertidos.

## Endpoints da API:

Para usar a API do Coin Snark localmente, você pode fazer solicitações para os seguintes endpoints:

Obter Lista de Moedas Suportadas:
```bash
curl "http://localhost:8000/api/currency"
```

Converter Moeda:
```bash
curl "http://localhost:8000/api/convert?from=usd&to=brl&amount=42.75"
```

Para obter informações mais detalhadas sobre os endpoints e suas funcionalidades, consulte a [documentação central da API](https://rmottanet.gitbook.io/coinsnark).

> Chaves de API de serviços de terceiros podem ser necessárias para o funcionamento correto de determinadas funcionalidades da API.

## Contribuindo

Contribuições para o projeto da API do Coin Snark são bem-vindas! Se você tiver ideias para melhorias, solicitações de recursos ou relatórios de bugs, sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull.

Obrigado por considerar a API do Coin Snark para suas necessidades de conversão de moeda. Se você tiver alguma dúvida ou precisar de mais assistência, não hesite em entrar em contato. Feliz codificação! 🚀
