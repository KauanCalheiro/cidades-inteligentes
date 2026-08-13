# Aula 02 — Cidades inteligentes, resilientes e sustentáveis (dados e certificação)

Resumo da transcrição ([transcricao.md](transcricao.md)). A transcrição é automática e não
traz nome de falante; nomes próprios foram corrigidos aqui (Lajeado, Teutônia, Bright Cities,
Connected Smart Cities, TACI, SROI).

## Recados

- **Grupos:** sete pessoas ainda sem grupo. Enquanto o nome não aparecer na planilha, o
  professor **zera as atividades**. Trabalho individual só combinando com ele antes.
- **Entrega 1:** o prazo era esta sexta, mas ele só corrige a partir de segunda, então
  atrasar um pouco não queima. **Só uma pessoa do grupo entrega.** Colega que não trabalha:
  avisar no chat, reflete na nota.
- **Semana 3 (próxima sexta):** sem encontro ao vivo. Estudos independentes com o curso da
  Escola Virtual de Governo sobre normas (dá certificado). Ele deve gravar uns 5 minutos de
  orientação e ainda vai definir a atividade, provavelmente conectada à cidade do grupo.
- **Cidade não muda.** Se o grupo quiser trocar, precisa avisar e justificar.
- Aula 4 volta à Carta Brasileira com atividade própria e trata de governança; aula 5 pega
  infraestrutura e retoma o framework TACI.

## Conteúdo da aula

**Linha do tempo:** anos 1980 aparecem as "comunidades inteligentes" (guidebook de San Diego),
Amsterdã é o primeiro case de grande alcance, Barcelona vira referência, **2014 sai a ISO 37120**
(primeira norma da série). No Brasil, **PL de 2021 da Política Nacional de Cidades Inteligentes**,
Curitiba puxando eventos e São Paulo publicando documentação técnica que serve de inspiração.

**Normas.** No catálogo da ABNT, buscar "cidades inteligentes" traz 3 resultados; buscar
**"smart cities" traz cerca de 80**. Normas custam caro e boa parte está fora da realidade dos
municípios brasileiros, por isso a maioria usa documentos que referenciam as normas em vez de
comprá-las. Sempre conferir se a versão ainda está vigente. As três da série:

| Norma | Foco |
|---|---|
| ISO 37120 | indicadores de serviços urbanos e qualidade de vida, conectados aos ODS |
| ISO 37122 | indicadores de cidade inteligente: mobilidade, governo digital, conectividade, dados abertos, gestão |
| ISO 37123 | indicadores de cidade resiliente: resistir, absorver e se adaptar a choques (as cheias da nossa região) |

**Certificação ABNT.** Baseada nessas três normas, cobre **19 setores** (economia, transporte,
educação, saúde, governança, segurança, finanças e mais 12) e vai de **bronze a platina**, com
reavaliação normalmente anual e caráter evolutivo: a cidade pede indicadores adicionais para
subir de nível. A cidade precisa não só comprovar que a política existe, mas apresentar dados
padronizados, auditáveis e validados por organismos independentes. Motivação por trás disso é
política e econômica: atrair investimento e ter comparação global.

**Alerta dele:** o tema atrai muito amador vendendo framework para prefeitura. "Abre o olho."

**Documento da UNESCO "Cidades MIL"** (alfabetização midiática e informacional), recente e já
compartilhado. Mostra como preparar a população, ofertar cursos e conectividade se conecta com
o resto, e organiza ações por ator: governo local, educação, saúde, transporte, indústria,
setor privado, ONGs, famílias.

**Ranqueadores.** Cada um tem sua metodologia e um pé em marketing. O **Connected Smart Cities**
é o mais conhecido; a edição **2025** se declara baseada em ISO, usa notas de 0 a 100 ponderadas
por valores de referência e metas dos ODS, e segue seleção de indicadores → eixos temáticos →
coleta → análise comparativa → ponderação e classificação. **Lajeado entrou entre as 10 cidades
destaque** por evolução em relação à edição anterior, com foco em governo inteligente.

**TACI (Tecnologias Avançadas para a Cidade Ideal).** Framework com a Cisco por trás, será
retomado na aula 5. Pilares: IoT e AIoT (iluminação, coleta de lixo, tráfego), **gêmeos digitais**
(por exemplo simular cheias em Lajeado), **IA generativa e agêntica**, **big data e blockchain**.
Ele posiciona a TI aí como **smart 6.0**, que integra tecnologia e participação cidadã (semana
passada ele tinha parado no 5.0; a numeração varia conforme o autor, não é norma).

**SROI, retorno social sobre investimento.** Em cidade o ROI clássico não serve. A conta é
**(ganhos tangíveis + intangíveis) / investimento, ao longo do tempo**. Intangíveis: confiança do
cidadão, inclusão social, participação, redução de desigualdades, resiliência institucional,
vantagem competitiva frente a outras cidades. Isso vale para o projeto final: nada de
investimento gigantesco com impacto real pequeno ou restrito a poucas pessoas.

**Ética, dados e o papel do desenvolvedor.** Algoritmos sem viés, transparência, LGPD e
privacidade por padrão desde o sensor de tráfego até o sistema integrado ("privacidade não é
barreira, é valor estratégico"), gestão contínua de vulnerabilidades. Cidade segura digitalmente
é a que trata segurança como política pública. Quem desenvolve para cidade inteligente precisa
conhecer minimamente a lógica das normas.

**Fontes de dados que ele mostrou** (depois de ter escondido tudo na semana 1):
**Bright Cities**, que avalia maturidade de municípios, permite comparar contra ~36 mil cidades
e gera gráfico de radar; plataforma inteligente com acesso gov.br voltada a prefeito e assessor;
TCE-RS; IBGE; bases de saúde, educação, meio ambiente e resiliência climática. Ressalva dele:
os números divergem entre plataformas, sempre checar de onde veio o dado.

Fechou mostrando um site interativo com exemplos de aplicação (lixeira que alerta a coleta,
caminhão que ajusta rota, RFID em prédio público, câmeras, redes de água e energia com menos
perdas, sensor de qualidade do ar) separados por transporte, utilities, telecom, governo e
ambiental, e o **Nível Guaíba**, uma página vibe coded que agregou dados das cheias.

## Entrega 2 — o que fazer

Documento **único** de **3 a 5 páginas**, com três partes que se conectam (não são três
trabalhos). Base **obrigatória**: o documento *Municípios Inteligentes, Humanos e Sustentáveis*,
cujos cinco níveis são **1 pessoas, 2 infraestrutura/serviços/redes, 3 território e economia
inteligente, 4 serviços e tecnologia da informação, 5 internet das coisas**.

1. **Proposta de integração técnica entre os níveis 2, 4 e 5** (~1 página): identificar a cidade,
   diagnosticar a infraestrutura (nível 2), a situação dos serviços públicos (nível 4) e a
   aplicação de IoT (nível 5). Entregar descrição crítica dos níveis, a proposta de integração e
   uma olhada em LGPD, sustentabilidade e impacto social.
2. **Dimensão humana** (~1 página): escolher **dois exemplos reais do documento** aplicáveis ao
   município, analisar como as decisões técnicas favorecem ou não a redução de desigualdades e
   discutir a participação cidadã na concepção, implantação e avaliação das soluções.
3. **Canvas de município inteligente** em **página única**, nove blocos, sintetizando diagnóstico
   e proposta. Pelos critérios que ele mostrou, é a parte de maior peso (citou quatro pontos).

**Regras:**

- **IA é liberada aqui**, ao contrário da entrega 1, desde que com transparência e informação
  conferida. Frase dele: a IA tem que fazer no mínimo melhor do que você faria sem ela. Canvas
  gerado por IA é aceito, desde que faça sentido e se conecte às etapas 1 e 2.
- **Documento extenso é devolvido e zerado.** Nada de despejar 10 ou 15 páginas de saída de LLM;
  vale também retroativamente para a entrega 1.
- Nada fora da realidade da cidade escolhida.
