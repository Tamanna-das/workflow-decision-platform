class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, payload):
        trace = []
        for rule in self.rules:
            field = rule["field"]
            op = rule["operator"]
            value = rule["value"]

            actual = payload.get(field)
            passed = eval(f"{actual} {op} {value}")

            trace.append({
                "rule": rule,
                "actual": actual,
                "passed": passed
            })

            if not passed:
                return rule["on_fail"], trace

        return "APPROVED", trace
