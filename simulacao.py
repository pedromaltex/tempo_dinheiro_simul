import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="⏱️ O Verdadeiro Valor do Teu Tempo",
    layout="centered"
)

st.title("⏱️ O Verdadeiro Valor do Teu Tempo")

tab1, tab2 = st.tabs([
    "🧾 A Tua Realidade",
    "📈 Resultados"
])

# =====================================================
# TAB 1 — A TUA REALIDADE (FOCO EM ACUMULAÇÃO)
# =====================================================

with tab1:

    st.header("💼 Rendimento e Tempo")

    rendimento = st.number_input("Salário mensal líquido (€)", 0.0, value=1200.0)
    horas_semanais = st.number_input("Horas trabalhadas por semana", 1, value=40)
    semanas_mes = 4.34821

    horas_mensais = horas_semanais * semanas_mes
    valor_hora_bruto = rendimento / horas_mensais if horas_mensais > 0 else 0
    horas_ano = horas_mensais * 12

    st.divider()

    st.header("🏠 Despesas Mensais")

    col1, col2 = st.columns(2)

    with col1:
        renda = st.number_input("Renda / Habitação (€)", 0.0, value=450.0)
        supermercado = st.number_input("Supermercado (€)", 0.0, value=250.0)
        transporte = st.number_input("Transportes (€)", 0.0, value=200.0)

    with col2:
        contas = st.number_input("Contas (luz, água, net) (€)", 0.0, value=150.0)
        lazer = st.number_input("Lazer (€)", 0.0, value=0.0)
        outros = st.number_input("Outros (€)", 0.0, value=0.0)

    despesas = renda + supermercado + transporte + contas + lazer + outros
    sobra = rendimento - despesas
    valor_hora_real = sobra / horas_mensais if horas_mensais > 0 else 0

    st.write(f"Total despesas: **{despesas:.2f} €**")
    st.write(f"Sobra mensalmente: **{sobra:.2f} €**")

    st.divider()

    st.header("🧠 O Valor do Teu Tempo")

    anos = st.slider("Anos a viver assim", 1, 50, 40)

    valor_acumulado = sobra * 12 * anos
    horas_vida = horas_ano * anos
    valor_acumulado_hora = valor_acumulado / horas_vida if horas_vida > 0 else 0

    colA, colB, colC = st.columns(3)

    colA.metric(
        "💰 Valor acumulado da tua vida",
        f"{valor_acumulado:,.0f} €",
        delta=f"{valor_acumulado_hora:.2f} € / hora de trabalho"
    )
    colB.metric("€ gerados por hora", f"{valor_hora_bruto:.2f} €")

    colC.metric(
        "€ acumulados por hora (hoje)",
        f"{valor_hora_real:.2f} €"
    )

    if sobra < 0:
        st.error("Estás a trabalhar para sobreviver. O tempo está contra ti.")
    elif valor_acumulado_hora < 1:
        st.warning("Uma vida inteira e cada hora trabalhada vale menos que um café.")
    elif valor_acumulado_hora < 3:
        st.info("Acumulas lentamente. Pequenas decisões mudam tudo.")
    else:
        st.success("Consegues poupar tempo e dinheiro assim.")

# =====================================================
# TAB 2 — DECISÕES DO DIA A DIA
# =====================================================

with tab2:

    st.subheader("🍽️ Quanto tempo algo te está a custar?")

    custo = 20

    if valor_hora_real <= 0:
        st.error("Tens de conseguir poupar para experimentar esta simulação.")
    else:
        horas = custo / valor_hora_real
        dias = horas / 8
        mes = dias / 30
        semanas = dias / 7
        anos = dias / 365.25

        if anos > 1:
            st.info(f"Um jantar de 20€ custa-te {anos:.1f} anos de trabalho.")
        elif mes > 1:
            st.info(f"Um jantar de 20€ custa-te {mes:.1f} meses de trabalho.")
        elif semanas > 1:
            st.info(f"Um jantar de 20€ custa-te {semanas:.1f} semanas de trabalho.")
        elif dias > 1:
            st.info(f"Um jantar de 20€ custa-te {dias:.1f} dias de trabalho.")
        else:
            st.info(f"Um jantar de 20€ custa-te {horas:.1f} horas de trabalho.")



    # =====================================================
    # TAB 3 — O TEMPO QUE SE VALORIZA (COMPACTA)
    # =====================================================



    st.subheader("🧠 Investir Tempo em Ti")

    horas_dia = 1

    aumento_salario = 300

    horas_ano = horas_dia * 365

    if horas_ano == 0:
        st.info("Sem investir tempo, o valor da tua hora mantém-se linear.")
    else:
        ganho_anual = aumento_salario * 12
        st.info(f"Se investires **1 hora** a aprender uma nova competência que te pague **{aumento_salario}€** no futuro isso quer"
                f" dizer que por cada hora investida, conseguiste acumular **{(ganho_anual / horas_ano):.2f} €** por hora gasta." )

    # =====================================================
    # INVESTIMENTO FINANCEIRO — CORRIGIDO
    # =====================================================
    st.subheader("💸 Dinheiro a Trabalhar para Ti")

    st.info(f"E se investires as tuas poupanças?")

    taxa = 0.08
    anos = st.slider("Anos", 1, 50, 30)

    poupanca_anual = max(sobra, 0) * 12
    horas_trabalhada_ano = horas_mensais * 12    



    if poupanca_anual <= 0:
        st.error("Sem poupança, o tempo continua linear.")
    else:
        valor = 0
        valor_hora = []

        carteira = []
        for i in range(1, anos + 1):
            valor = (valor + poupanca_anual) * (1 + taxa)
            carteira.append(valor)
            horas_totais = horas_trabalhada_ano * i
            valor_hora.append(valor / (horas_totais if horas_totais > 0 else 1))

        col1, col2 = st.columns(2)

        v_hora = poupanca_anual / (horas_trabalhada_ano) if horas_trabalhada_ano > 0 else 0

        ratio = valor_hora[-1] / v_hora

        st.success(f"Investiste durante **{anos} anos**. Isso permitiu-te que o teu valor acumulado à hora fosse **{ratio:.1f}** vezes superior!")


        col1.metric("Total investido", f"{poupanca_anual * anos:,.0f} €",
                    delta=f"{v_hora if anos > 0 else 0:.2f} € / hora de trabalho")

        col2.metric("Valor acumulado", f"{valor:,.0f} €",
                    delta=f"{valor_hora[-1]:.2f} € / hora de trabalho")

        investido = [poupanca_anual * i for i in range(1, anos + 1)]

        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(range(1, anos + 1)),
            y=carteira,
            mode="lines",
            line=dict(width=3),
            name="€ acumulados por hora de vida"
        ))

        fig.add_trace(go.Scatter(
            x=list(range(1, anos + 1)),
            y=investido,
            mode="lines",
            name="Apenas dinheiro colocado",
            line=dict(dash="dash")
        ))

        fig.update_layout(
            title="Cada Hora da Tua Vida Fica Mais Valiosa",
            xaxis_title="Ano",
            yaxis_title="€ acumulados por hora de vida",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

import streamlit.components.v1 as components

components.html(
    """
    <script type="text/javascript"
        src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js"
        data-name="bmc-button"
        data-slug="pedromoraia"
        data-color="#FFDD00"
        data-emoji=""
        data-font="Cookie"
        data-text="Ajuda-nos a ajudar"
        data-outline-color="#000000"
        data-font-color="#000000"
        data-coffee-color="#ffffff">
    </script>
    """,
    height=80
)
