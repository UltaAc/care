from pydantic.main import BaseModel

from care.emr.fhir.resources.base import ResourceManger
from care.emr.fhir.utils import parse_fhir_parameter_output


class CodeConceptResource(ResourceManger):
    allowed_properties = ["system", "code"]
    resource = "CodeConcept"

    def serialize_lookup(self, result):
        structured_output = parse_fhir_parameter_output(result)
        return CodeConcept(
            name=structured_output["name"],
            display=structured_output["display"],
            code=self._filters["code"],
            system=structured_output["system"],
            property=structured_output.get("property", {}),
            designation=structured_output.get("designation", {}) or {},
        )

    def get(self):
        if "system" not in self._filters or "code" not in self._filters:
            err = "Both system and code are required"
            raise ValueError(err)
        full_result = self.query("GET", "CodeSystem/$lookup", self._filters)
        return self.serialize_lookup(full_result["parameter"])


class MinimalCodeConcept(BaseModel):
    display: str
    system: str
    code: str


class CodeConcept(MinimalCodeConcept):
    name: str
    property: dict
    designation: dict
