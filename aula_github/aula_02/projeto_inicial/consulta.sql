-- Consulta de exemplo para relatorios
SELECT cliente_id, SUM(valor) as total_gasto
FROM transacoes
WHERE status = 'APROVADO'
GROUP BY cliente_id;