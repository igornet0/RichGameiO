type_event = {
        "cyberattack": """Влияние: Крупная кибератака приводит к 
                            утечке данных и потере 10% средств у игроков.
                        Результат: У игроков, чьи аккаунты были скомпрометированы, могут быть 
                            украдены средства в размере 10% .
                        Расчет: Если игрок заходит в казино с 20% вероятностью его аккаунт
                            будет скомпрометирован, он может потерять 10% RichCoin от общих средсв""",

        "newcoin": """Влияние: В сети Badcoin выходит новая монета, 
                            для получения 1 новой монеты до листинга, нужно сжечь N RichCoin.
                        Результат: Игроки которые сожгли RichCoin, 
                            после листинга за N RichCoin получат 1 новую монету.
                        Расчет: 1 новая монета после листинга стоит N + K1 RichCoin""",

        "government": """Влияние: Правительство объявляет о запрете
                            использования определенных криптовалют в стране.
                        Результат: Цены на запрещенные криптовалюты в игре падают на 50%, 
                        которые объявят через N часов.
                        Расчет: Если игрок владел запрещенной криптовалюты стоимостью, 
                            его капитал уменьшится на 50%.""",

        "taxes": """Влияние: ЦБ объявляет о повышение налогов.
                        Результат: прибыль с бизнеса уменьшается на N%.
                        Расчет: Если игрок владел бизнесом, его доход в день, уменьшается на N%.""",
    }

#percent_add_price
PAC = 10

list_items = {
        "phone":            {"price": 100, "profit": 10},
        "mining station":   {"price": 2500, "profit": 20},
        "car":              {"price": 5000, "profit": 40},
        "parking":          {"price": 3000, "profit": 50},
        "garage":           {"price": 5000, "profit": 60},
        "room":             {"price": 10000, "profit": 80},
        "flat":             {"price": 15000, "profit": 100},
        "house":            {"price": 20000, "profit": 150},
        "friends":          {"price":0 , "profit":0}
}

list_business = {
        "miningfarm phone": {"Xprofit": 1.2, "taxes": 0, "price": 50},
        "miningfarm":       {"Xprofit": 1.5, "taxes": 5, "price": 500},
        "taxi":             {"Xprofit": 1.8, "taxes": 10, "price": 1500},
        "office":           {"Xprofit": 2, "taxes": 15, "price": 3000},
        "restaurant":       {"Xprofit": 2.5, "taxes": 15, "price": 5000},
        "bank":             {"Xprofit": 2, "taxes": 10, "price": 10000},
        "crypto exchange":  {"Xprofit": 1, "profit": 100, "taxes": 0, "price": 0},
    }

cost_business_items = {
        "miningfarm phone": {"phone": 100},
        "miningfarm":       {"mining station": 100},
        "taxi":             {"car": 100},
        "office":           {"flat": 10},
        "restaurant":       {"room": 10},
        "bank":             {"house": 2},
        "crypto exchange":  {"friends": 10},
    }