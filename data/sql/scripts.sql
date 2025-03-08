select count(*) from raw_cryptos rc;
select count(*) from currated_cryptos cc;
select count(*) from enriched_cryptos ec;

drop table currated_cryptos;

SELECT *
FROM enriched_cryptos ec 
WHERE ec.current_price_brl >= 1000
ORDER BY ec.current_price_brl DESC;

SELECT name, symbol, current_price_brl, market_cap_brl
FROM enriched_cryptos
ORDER BY current_price_brl DESC
LIMIT 10;

SELECT name, symbol, current_price_brl, market_cap_brl, total_volume_brl
FROM enriched_cryptos
WHERE market_cap_brl > 1_000_000  -- Exclui market cap abaixo de R$ 1 milhão
AND total_volume_brl > 10_000     -- Exclui criptos que ninguém negocia
ORDER BY current_price_brl DESC;


SELECT 
	ec.name as 'Nome_Crypto',
	ec.symbol as 'Simbolo_Crypto',
	ec.market_cap_rank as 'Posicao_Ranking_Valor_Mercado',
	ec.current_price_brl as 'Preco_Atual_BRL',
	ec.total_volume_brl as 'Volume_Total_BRL',
	ec.high_24h_brl as 'Maior_Preco_24h',
	ec.low_24h_brl as 'Menor_Preco_24h',
	ec.circulating_supply as 'Fornecimento_Circulante'
FROM enriched_cryptos ec
WHERE market_cap_brl > 1_000_000    -- Exclui market cap abaixo de R$ 1 milhão
AND total_volume_brl > 1_000_000    -- Exclui criptos que quase ninguém negocia
-- AND name NOT LIKE '%Bitcoin%'
AND name NOT LIKE '%BTC%'
AND name NOT LIKE '%Wrapped%'
ORDER BY current_price_brl DESC;

SELECT 
	ec.name as 'Nome_Crypto',
	ec.symbol as 'Simbolo_Crypto',
	ec.market_cap_rank as 'Posicao_Ranking_Valor_Mercado',
	ec.current_price_brl as 'Preco_Atual_BRL',
	ec.total_volume_brl as 'Volume_Total_BRL',
	ec.high_24h_brl as 'Maior_Preco_24h',
	ec.low_24h_brl as 'Menor_Preco_24h',
	ec.circulating_supply as 'Fornecimento_Circulante'
FROM enriched_cryptos ec
WHERE market_cap_brl > 1_000_000    -- Exclui market cap abaixo de R$ 1 milhão
AND total_volume_brl > 1_000_000    -- Exclui criptos que quase ninguém negocia
-- AND name NOT LIKE '%Bitcoin%'
AND name NOT LIKE '%BTC%'
AND name NOT LIKE '%Wrapped%'
ORDER BY market_cap_rank;


SELECT 
	ec.name as 'Nome_Crypto',
	ec.symbol as 'Simbolo_Crypto',
	ec.market_cap_rank as 'Posicao_Ranking_Valor_Mercado',
	ec.circulating_supply as 'Fornecimento_Circulante',
	ec.current_price,
	ec.high_24h,
	ec.low_24h,
	ec.price_change_percentage_24h,
	ec.price_change_24h,
	timestamp
FROM raw_cryptos ec
where price_change_percentage_24h is not null 
and Posicao_Ranking_Valor_Mercado is not null
AND name NOT LIKE '%BTC%'
AND name NOT LIKE '%Wrapped%'
AND current_price >= 1
ORDER BY price_change_percentage_24h, ec.timestamp  DESC
LIMIT 100;

SELECT 
	ec.name as 'Nome_Crypto',
	ec.symbol as 'Simbolo_Crypto',
	ec.market_cap_rank as 'Posicao_Ranking_Valor_Mercado',
	ec.circulating_supply as 'Fornecimento_Circulante',
	ec.current_price,
	ec.high_24h,
	ec.low_24h,
	 ec.price_change_percentage_24h,
	 ec.price_change_24h 
FROM raw_cryptos ec
where price_change_percentage_24h is not null 
and Posicao_Ranking_Valor_Mercado is not null
AND name NOT LIKE '%BTC%'
AND name NOT LIKE '%Wrapped%'
AND current_price >= 1
ORDER BY price_change_percentage_24h asc
LIMIT 10;
