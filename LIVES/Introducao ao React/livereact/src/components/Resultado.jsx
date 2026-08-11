import '../css/global.css'
import '../css/resultado.css'


// TABELA
const TABELA_IMC = [
    { id: "abaixo", limite: 18.5, classificacao: "abaixo do peso", faixa: "abaixo de 18.5" },
    { id: "normal", limite: 25, classificacao: "Dentro do peso", faixa: "18.5 - 24.9" },
    { id: "acima", limite: 30, classificacao: "acima do peso", faixa: "25 - 29.9" },
]

const Resultado = ({ resultado }) => {
    const valor = parseFloat(resultado)

    return (
        <section className='imc-container'>
            <table className='imc-table'>
                <thead>
                    <tr>
                        <th>Classificacao</th>
                        <th>IMC</th>
                    </tr>
                </thead>
                <tbody>
                    {TABELA_IMC.map((item, index) => {
                        const limiteAnterior = index > 0 ? TABELA_IMC[index - 1].limite : 0;
                        const isAtivo = !isNaN(valor) && valor >= limiteAnterior && valor < item.limite;

                        return (
                            <tr key={item.id} className={isAtivo ? "destaque" : ""}>
                                <td>{item.classificacao}</td>
                                <td>{item.faixa}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </section>
    )
}

export default Resultado
