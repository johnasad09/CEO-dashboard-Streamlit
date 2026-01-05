from dataclasses import dataclass

@dataclass
class Metric:
    title: str
    func: callable # type: ignore
    type: str  # 'number' or 'chart'
