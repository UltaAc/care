# ruff: noqa: N815 F405 - Naming convention is disabled for this file because it needs to match the FHIR schema
# Partly generated from fhir.schema.json R5 on 2024-11-09

from __future__ import annotations

from enum import Enum

from typing import Any, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, constr

class Base64Binary(RootModel[str]):
    root: str = Field(..., description='A stream of bytes')


class Boolean(RootModel[bool]):
    root: bool = Field(..., description='Value of "true" or "false"')


class Canonical(RootModel[constr(pattern=r'^\S*$')]):
    root: constr(pattern=r'^\S*$') = Field(
        ...,
        description='A URI that is a reference to a canonical URL on a FHIR resource',
    )


class Code(RootModel[constr(pattern=r'^[^\s]+( [^\s]+)*$')]):
    root: constr(pattern=r'^[^\s]+( [^\s]+)*$') = Field(
        ...,
        description='A string which has at least one character and no leading or trailing whitespace and where there is no whitespace other than single spaces in the contents',
    )


class Date(
    RootModel[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?$'
        )
    ]
):
    root: constr(
        pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?$'
    ) = Field(
        ...,
        description='A date or partial date (e.g. just year or year + month). There is no UTC offset. The format is a union of the schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.',
    )


class DateTime(
    RootModel[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?)?)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)?)?)?$'
        )
    ]
):
    root: constr(
        pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?)?)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)?)?)?$'
    ) = Field(
        ...,
        description='A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a UTC offset SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates SHALL be valid dates.',
    )


class Decimal(RootModel[float]):
    root: float = Field(..., description='A rational number with implicit precision')


class Id(RootModel[constr(pattern=r'^[A-Za-z0-9\-\.]{1,64}$')]):
    root: constr(pattern=r'^[A-Za-z0-9\-\.]{1,64}$') = Field(
        ...,
        description='Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-insensitive.',
    )


class Instant(
    RootModel[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$'
        )
    ]
):
    root: constr(
        pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$'
    ) = Field(..., description='An instant in time - known at least to the second')


class Integer(RootModel[float]):
    root: float = Field(..., description='A whole number')


class Integer64(RootModel[constr(pattern=r'^[0]|[-+]?[1-9][0-9]*$')]):
    root: constr(pattern=r'^[0]|[-+]?[1-9][0-9]*$') = Field(
        ..., description='A very large whole number'
    )


class Markdown(RootModel[constr(pattern=r'^^[\s\S]+$$')]):
    root: constr(pattern=r'^^[\s\S]+$$') = Field(
        ...,
        description='A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation engine',
    )


class Oid(RootModel[constr(pattern=r'^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$')]):
    root: constr(pattern=r'^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$') = Field(
        ..., description='An OID represented as a URI'
    )


class PositiveInt(RootModel[float]):
    root: float = Field(
        ..., description='An integer with a value that is positive (e.g. >0)'
    )


class String(RootModel[constr(pattern=r'^^[\s\S]+$$')]):
    root: constr(pattern=r'^^[\s\S]+$$') = Field(
        ..., description='A sequence of Unicode characters'
    )


class Time(
    RootModel[
        constr(
            pattern=r'^([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?$'
        )
    ]
):
    root: constr(
        pattern=r'^([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?$'
    ) = Field(..., description='A time during the day, with no date specified')


class UnsignedInt(RootModel[float]):
    root: float = Field(
        ..., description='An integer with a value that is not negative (e.g. >= 0)'
    )


class Uri(RootModel[constr(pattern=r'^\S*$')]):
    root: constr(pattern=r'^\S*$') = Field(
        ..., description='String of characters used to identify a name or a resource'
    )

class Url(RootModel[constr(pattern=r'^\S*$')]):
    root: constr(pattern=r'^\S*$') = Field(
        ..., description='A URI that is a literal reference'
    )


class Uuid(
    RootModel[
        constr(
            pattern=r'^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        )
    ]
):
    root: constr(
        pattern=r'^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    ) = Field(..., description='A UUID, represented as a URI')


class Xhtml(RootModel[Any]):
    root: Any = Field(..., description='xhtml - escaped html (see specfication)')


class Base(BaseModel):
    pass
    model_config = ConfigDict(
        extra='forbid',
    )


class Status(Enum):
    generated = 'generated'
    extensions = 'extensions'
    additional = 'additional'
    empty = 'empty'


class Use(Enum):
    usual = 'usual'
    official = 'official'
    temp = 'temp'
    secondary = 'secondary'
    old = 'old'


class Comparator(Enum):
    field_ = '<'
    field__ = '<='
    field___1 = '>='
    field__1 = '>'
    ad = 'ad'


class Use1(Enum):
    usual = 'usual'
    official = 'official'
    temp = 'temp'
    nickname = 'nickname'
    anonymous = 'anonymous'
    old = 'old'
    maiden = 'maiden'


class Use2(Enum):
    home = 'home'
    work = 'work'
    temp = 'temp'
    old = 'old'
    billing = 'billing'


class Type(Enum):
    postal = 'postal'
    physical = 'physical'
    both = 'both'


class System(Enum):
    phone = 'phone'
    fax = 'fax'
    email = 'email'
    pager = 'pager'
    url = 'url'
    sms = 'sms'
    other = 'other'


class Use3(Enum):
    home = 'home'
    work = 'work'
    temp = 'temp'
    old = 'old'
    mobile = 'mobile'


class DurationUnit(Enum):
    s = 's'
    min = 'min'
    h = 'h'
    d = 'd'
    wk = 'wk'
    mo = 'mo'
    a = 'a'


class PeriodUnit(Enum):
    s = 's'
    min = 'min'
    h = 'h'
    d = 'd'
    wk = 'wk'
    mo = 'mo'
    a = 'a'


class WhenEnum(Enum):
    MORN = 'MORN'
    MORN_early = 'MORN.early'
    MORN_late = 'MORN.late'
    NOON = 'NOON'
    AFT = 'AFT'
    AFT_early = 'AFT.early'
    AFT_late = 'AFT.late'
    EVE = 'EVE'
    EVE_early = 'EVE.early'
    EVE_late = 'EVE.late'
    NIGHT = 'NIGHT'
    PHS = 'PHS'
    IMD = 'IMD'
    HS = 'HS'
    WAKE = 'WAKE'
    C = 'C'
    CM = 'CM'
    CD = 'CD'
    CV = 'CV'
    AC = 'AC'
    ACM = 'ACM'
    ACD = 'ACD'
    ACV = 'ACV'
    PC = 'PC'
    PCM = 'PCM'
    PCD = 'PCD'
    PCV = 'PCV'


class Type1(Enum):
    author = 'author'
    editor = 'editor'
    reviewer = 'reviewer'
    endorser = 'endorser'


class Direction(Enum):
    ascending = 'ascending'
    descending = 'descending'


class Type2(Enum):
    documentation = 'documentation'
    justification = 'justification'
    citation = 'citation'
    predecessor = 'predecessor'
    successor = 'successor'
    derived_from = 'derived-from'
    depends_on = 'depends-on'
    composed_of = 'composed-of'
    part_of = 'part-of'
    amends = 'amends'
    amended_with = 'amended-with'
    appends = 'appends'
    appended_with = 'appended-with'
    cites = 'cites'
    cited_by = 'cited-by'
    comments_on = 'comments-on'
    comment_in = 'comment-in'
    contains = 'contains'
    contained_in = 'contained-in'
    corrects = 'corrects'
    correction_in = 'correction-in'
    replaces = 'replaces'
    replaced_with = 'replaced-with'
    retracts = 'retracts'
    retracted_by = 'retracted-by'
    signs = 'signs'
    similar_to = 'similar-to'
    supports = 'supports'
    supported_with = 'supported-with'
    transforms = 'transforms'
    transformed_into = 'transformed-into'
    transformed_with = 'transformed-with'
    documents = 'documents'
    specification_of = 'specification-of'
    created_with = 'created-with'
    cite_as = 'cite-as'


class Type3(Enum):
    named_event = 'named-event'
    periodic = 'periodic'
    data_changed = 'data-changed'
    data_added = 'data-added'
    data_modified = 'data-modified'
    data_removed = 'data-removed'
    data_accessed = 'data-accessed'
    data_access_ended = 'data-access-ended'


class RepresentationEnum(Enum):
    xmlAttr = 'xmlAttr'
    xmlText = 'xmlText'
    typeAttr = 'typeAttr'
    cdaText = 'cdaText'
    xhtml = 'xhtml'


class Rules(Enum):
    closed = 'closed'
    open = 'open'
    openAtEnd = 'openAtEnd'


class Type4(Enum):
    value = 'value'
    exists = 'exists'
    pattern = 'pattern'
    type = 'type'
    profile = 'profile'
    position = 'position'


class AggregationEnum(Enum):
    contained = 'contained'
    referenced = 'referenced'
    bundled = 'bundled'


class Versioning(Enum):
    either = 'either'
    independent = 'independent'
    specific = 'specific'


class Severity(Enum):
    error = 'error'
    warning = 'warning'


class Strength(Enum):
    required = 'required'
    extensible = 'extensible'
    preferred = 'preferred'
    example = 'example'



class Element(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )


class DataType(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )


class PrimitiveType(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )


class BackboneType(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.\n\nModifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )


class Extension(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    url: Optional[Uri] = Field(
        None,
        description='Source of the definition for the extension code - a logical name or a URL.',
    )
    field_url: Optional[Element] = Field(
        None, alias='_url', description='Extensions for url'
    )
    valueBase64Binary: Optional[
        constr(
            pattern=r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueBase64Binary: Optional[Element] = Field(
        None, alias='_valueBase64Binary', description='Extensions for valueBase64Binary'
    )
    valueBoolean: Optional[bool] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueBoolean: Optional[Element] = Field(
        None, alias='_valueBoolean', description='Extensions for valueBoolean'
    )
    valueCanonical: Optional[constr(pattern=r'^\S*$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueCanonical: Optional[Element] = Field(
        None, alias='_valueCanonical', description='Extensions for valueCanonical'
    )
    valueCode: Optional[constr(pattern=r'^[^\s]+( [^\s]+)*$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueCode: Optional[Element] = Field(
        None, alias='_valueCode', description='Extensions for valueCode'
    )
    valueDate: Optional[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueDate: Optional[Element] = Field(
        None, alias='_valueDate', description='Extensions for valueDate'
    )
    valueDateTime: Optional[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?)?)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)?)?)?$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueDateTime: Optional[Element] = Field(
        None, alias='_valueDateTime', description='Extensions for valueDateTime'
    )
    valueDecimal: Optional[float] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueDecimal: Optional[Element] = Field(
        None, alias='_valueDecimal', description='Extensions for valueDecimal'
    )
    valueId: Optional[constr(pattern=r'^[A-Za-z0-9\-\.]{1,64}$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueId: Optional[Element] = Field(
        None, alias='_valueId', description='Extensions for valueId'
    )
    valueInstant: Optional[
        constr(
            pattern=r'^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueInstant: Optional[Element] = Field(
        None, alias='_valueInstant', description='Extensions for valueInstant'
    )
    valueInteger: Optional[float] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueInteger: Optional[Element] = Field(
        None, alias='_valueInteger', description='Extensions for valueInteger'
    )
    valueInteger64: Optional[constr(pattern=r'^[0]|[-+]?[1-9][0-9]*$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueInteger64: Optional[Element] = Field(
        None, alias='_valueInteger64', description='Extensions for valueInteger64'
    )
    valueMarkdown: Optional[constr(pattern=r'^^[\s\S]+$$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueMarkdown: Optional[Element] = Field(
        None, alias='_valueMarkdown', description='Extensions for valueMarkdown'
    )
    valueOid: Optional[constr(pattern=r'^urn:oid:[0-2](\.(0|[1-9][0-9]*))+$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueOid: Optional[Element] = Field(
        None, alias='_valueOid', description='Extensions for valueOid'
    )
    valuePositiveInt: Optional[float] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valuePositiveInt: Optional[Element] = Field(
        None, alias='_valuePositiveInt', description='Extensions for valuePositiveInt'
    )
    valueString: Optional[constr(pattern=r'^^[\s\S]+$$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueString: Optional[Element] = Field(
        None, alias='_valueString', description='Extensions for valueString'
    )
    valueTime: Optional[
        constr(
            pattern=r'^([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]{1,9})?$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueTime: Optional[Element] = Field(
        None, alias='_valueTime', description='Extensions for valueTime'
    )
    valueUnsignedInt: Optional[float] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueUnsignedInt: Optional[Element] = Field(
        None, alias='_valueUnsignedInt', description='Extensions for valueUnsignedInt'
    )
    valueUri: Optional[constr(pattern=r'^\S*$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueUri: Optional[Element] = Field(
        None, alias='_valueUri', description='Extensions for valueUri'
    )
    valueUrl: Optional[constr(pattern=r'^\S*$')] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueUrl: Optional[Element] = Field(
        None, alias='_valueUrl', description='Extensions for valueUrl'
    )
    valueUuid: Optional[
        constr(
            pattern=r'^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        )
    ] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    field_valueUuid: Optional[Element] = Field(
        None, alias='_valueUuid', description='Extensions for valueUuid'
    )
    valueAddress: Optional[Address] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueAge: Optional[Age] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueAnnotation: Optional[Annotation] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueAttachment: Optional[Attachment] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueCodeableConcept: Optional[CodeableConcept] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueCodeableReference: Optional[CodeableReference] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueCoding: Optional[Coding] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueContactPoint: Optional[ContactPoint] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueCount: Optional[Count] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueDistance: Optional[Distance] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueDuration: Optional[Duration] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueHumanName: Optional[HumanName] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueIdentifier: Optional[Identifier] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueMoney: Optional[Money] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valuePeriod: Optional[Period] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueQuantity: Optional[Quantity] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueRange: Optional[Range] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueRatio: Optional[Ratio] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueRatioRange: Optional[RatioRange] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueReference: Optional[Reference] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueSampledData: Optional[SampledData] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueSignature: Optional[Signature] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueTiming: Optional[Timing] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueContactDetail: Optional[ContactDetail] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    # valueDataRequirement: Optional[DataRequirement] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    valueExpression: Optional[Expression] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    valueParameterDefinition: Optional[ParameterDefinition] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    # valueRelatedArtifact: Optional[RelatedArtifact] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    # valueTriggerDefinition: Optional[TriggerDefinition] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    valueUsageContext: Optional[UsageContext] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )
    # valueAvailability: Optional[Availability] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    # valueExtendedContactDetail: Optional[ExtendedContactDetail] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    # valueDosage: Optional[Dosage] = Field(
    #     None,
    #     description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    # )
    valueMeta: Optional[Meta] = Field(
        None,
        description='Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list).',
    )


class Narrative(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    status: Optional[Status] = Field(
        None,
        description="The status of the narrative - whether it's entirely generated (from just the defined data or the extensions too), or whether a human authored it and it may contain additional data.",
    )
    field_status: Optional[Element] = Field(
        None, alias='_status', description='Extensions for status'
    )
    div: Xhtml = Field(
        ...,
        description='The actual narrative content, a stripped down version of XHTML.',
    )


class Annotation(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    authorReference: Optional[Reference] = Field(
        None, description='The individual responsible for making the annotation.'
    )
    authorString: Optional[constr(pattern=r'^^[\s\S]+$$')] = Field(
        None, description='The individual responsible for making the annotation.'
    )
    field_authorString: Optional[Element] = Field(
        None, alias='_authorString', description='Extensions for authorString'
    )
    time: Optional[DateTime] = Field(
        None, description='Indicates when this particular annotation was made.'
    )
    field_time: Optional[Element] = Field(
        None, alias='_time', description='Extensions for time'
    )
    text: Optional[Markdown] = Field(
        None, description='The text of the annotation in markdown format.'
    )
    field_text: Optional[Element] = Field(
        None, alias='_text', description='Extensions for text'
    )


class Attachment(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    contentType: Optional[Code] = Field(
        None,
        description='Identifies the type of the data in the attachment and allows a method to be chosen to interpret or render the data. Includes mime type parameters such as charset where appropriate.',
    )
    field_contentType: Optional[Element] = Field(
        None, alias='_contentType', description='Extensions for contentType'
    )
    language: Optional[Code] = Field(
        None,
        description='The human language of the content. The value can be any valid value according to BCP 47.',
    )
    field_language: Optional[Element] = Field(
        None, alias='_language', description='Extensions for language'
    )
    data: Optional[Base64Binary] = Field(
        None,
        description='The actual data of the attachment - a sequence of bytes, base64 encoded.',
    )
    field_data: Optional[Element] = Field(
        None, alias='_data', description='Extensions for data'
    )
    url: Optional[Url] = Field(
        None, description='A location where the data can be accessed.'
    )
    field_url: Optional[Element] = Field(
        None, alias='_url', description='Extensions for url'
    )
    size: Optional[Integer64] = Field(
        None,
        description='The number of bytes of data that make up this attachment (before base64 encoding, if that is done).',
    )
    field_size: Optional[Element] = Field(
        None, alias='_size', description='Extensions for size'
    )
    hash: Optional[Base64Binary] = Field(
        None,
        description='The calculated hash of the data using SHA-1. Represented using base64.',
    )
    field_hash: Optional[Element] = Field(
        None, alias='_hash', description='Extensions for hash'
    )
    title: Optional[String] = Field(
        None, description='A label or set of text to display in place of the data.'
    )
    field_title: Optional[Element] = Field(
        None, alias='_title', description='Extensions for title'
    )
    creation: Optional[DateTime] = Field(
        None, description='The date that the attachment was first created.'
    )
    field_creation: Optional[Element] = Field(
        None, alias='_creation', description='Extensions for creation'
    )
    height: Optional[PositiveInt] = Field(
        None, description='Height of the image in pixels (photo/video).'
    )
    field_height: Optional[Element] = Field(
        None, alias='_height', description='Extensions for height'
    )
    width: Optional[PositiveInt] = Field(
        None, description='Width of the image in pixels (photo/video).'
    )
    field_width: Optional[Element] = Field(
        None, alias='_width', description='Extensions for width'
    )
    frames: Optional[PositiveInt] = Field(
        None,
        description='The number of frames in a photo. This is used with a multi-page fax, or an imaging acquisition context that takes multiple slices in a single image, or an animated gif. If there is more than one frame, this SHALL have a value in order to alert interface software that a multi-frame capable rendering widget is required.',
    )
    field_frames: Optional[Element] = Field(
        None, alias='_frames', description='Extensions for frames'
    )
    duration: Optional[Decimal] = Field(
        None,
        description='The duration of the recording in seconds - for audio and video.',
    )
    field_duration: Optional[Element] = Field(
        None, alias='_duration', description='Extensions for duration'
    )
    pages: Optional[PositiveInt] = Field(
        None, description='The number of pages when printed.'
    )
    field_pages: Optional[Element] = Field(
        None, alias='_pages', description='Extensions for pages'
    )


class Identifier(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    use: Optional[Use] = Field(None, description='The purpose of this identifier.')
    field_use: Optional[Element] = Field(
        None, alias='_use', description='Extensions for use'
    )
    type: Optional[CodeableConcept] = Field(
        None,
        description='A coded type for the identifier that can be used to determine which identifier to use for a specific purpose.',
    )
    system: Optional[Uri] = Field(
        None,
        description='Establishes the namespace for the value - that is, an absolute URL that describes a set values that are unique.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    value: Optional[String] = Field(
        None,
        description='The portion of the identifier typically relevant to the user and which is unique within the context of the system.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    period: Optional[Period] = Field(
        None, description='Time period during which identifier is/was valid for use.'
    )
    assigner: Optional[Reference] = Field(
        None, description='Organization that issued/manages the identifier.'
    )


class CodeableConcept(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    coding: Optional[List[Coding]] = Field(
        None, description='A reference to a code defined by a terminology system.'
    )
    text: Optional[String] = Field(
        None,
        description='A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user.',
    )
    field_text: Optional[Element] = Field(
        None, alias='_text', description='Extensions for text'
    )


class CodeableReference(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    concept: Optional[CodeableConcept] = Field(
        None,
        description='A reference to a concept - e.g. the information is identified by its general class to the degree of precision found in the terminology.',
    )
    reference: Optional[Reference] = Field(
        None,
        description='A reference to a resource the provides exact details about the information being referenced.',
    )


class Coding(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the code system that defines the meaning of the symbol in the code.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    version: Optional[String] = Field(
        None,
        description='The version of the code system which was used when choosing this code. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.',
    )
    field_version: Optional[Element] = Field(
        None, alias='_version', description='Extensions for version'
    )
    code: Optional[Code] = Field(
        None,
        description='A symbol in syntax defined by the system. The symbol may be a predefined code or an expression in a syntax defined by the coding system (e.g. post-coordination).',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )
    display: Optional[String] = Field(
        None,
        description='A representation of the meaning of the code in the system, following the rules of the system.',
    )
    field_display: Optional[Element] = Field(
        None, alias='_display', description='Extensions for display'
    )
    userSelected: Optional[Boolean] = Field(
        None,
        description='Indicates that this coding was chosen by a user directly - e.g. off a pick list of available items (codes or displays).',
    )
    field_userSelected: Optional[Element] = Field(
        None, alias='_userSelected', description='Extensions for userSelected'
    )


class Quantity(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None,
        description='The value of the measured amount. The value includes an implicit precision in the presentation of the value.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    comparator: Optional[Comparator] = Field(
        None,
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.',
    )
    field_comparator: Optional[Element] = Field(
        None, alias='_comparator', description='Extensions for comparator'
    )
    unit: Optional[String] = Field(
        None, description='A human-readable form of the unit.'
    )
    field_unit: Optional[Element] = Field(
        None, alias='_unit', description='Extensions for unit'
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the system that provides the coded form of the unit.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    code: Optional[Code] = Field(
        None,
        description='A computer processable form of the unit in some unit representation system.',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )


class Duration(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None,
        description='The value of the measured amount. The value includes an implicit precision in the presentation of the value.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    comparator: Optional[Comparator] = Field(
        None,
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.',
    )
    field_comparator: Optional[Element] = Field(
        None, alias='_comparator', description='Extensions for comparator'
    )
    unit: Optional[String] = Field(
        None, description='A human-readable form of the unit.'
    )
    field_unit: Optional[Element] = Field(
        None, alias='_unit', description='Extensions for unit'
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the system that provides the coded form of the unit.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    code: Optional[Code] = Field(
        None,
        description='A computer processable form of the unit in some unit representation system.',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )


class Distance(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None,
        description='The value of the measured amount. The value includes an implicit precision in the presentation of the value.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    comparator: Optional[Comparator] = Field(
        None,
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.',
    )
    field_comparator: Optional[Element] = Field(
        None, alias='_comparator', description='Extensions for comparator'
    )
    unit: Optional[String] = Field(
        None, description='A human-readable form of the unit.'
    )
    field_unit: Optional[Element] = Field(
        None, alias='_unit', description='Extensions for unit'
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the system that provides the coded form of the unit.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    code: Optional[Code] = Field(
        None,
        description='A computer processable form of the unit in some unit representation system.',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )


class Count(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None,
        description='The value of the measured amount. The value includes an implicit precision in the presentation of the value.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    comparator: Optional[Comparator] = Field(
        None,
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.',
    )
    field_comparator: Optional[Element] = Field(
        None, alias='_comparator', description='Extensions for comparator'
    )
    unit: Optional[String] = Field(
        None, description='A human-readable form of the unit.'
    )
    field_unit: Optional[Element] = Field(
        None, alias='_unit', description='Extensions for unit'
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the system that provides the coded form of the unit.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    code: Optional[Code] = Field(
        None,
        description='A computer processable form of the unit in some unit representation system.',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )


class Money(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None, description='Numerical value (with implicit precision).'
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    currency: Optional[Code] = Field(None, description='ISO 4217 Currency Code.')
    field_currency: Optional[Element] = Field(
        None, alias='_currency', description='Extensions for currency'
    )


class Age(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    value: Optional[Decimal] = Field(
        None,
        description='The value of the measured amount. The value includes an implicit precision in the presentation of the value.',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    comparator: Optional[Comparator] = Field(
        None,
        description='How the value should be understood and represented - whether the actual value is greater or less than the stated value due to measurement issues; e.g. if the comparator is "<" , then the real value is < stated value.',
    )
    field_comparator: Optional[Element] = Field(
        None, alias='_comparator', description='Extensions for comparator'
    )
    unit: Optional[String] = Field(
        None, description='A human-readable form of the unit.'
    )
    field_unit: Optional[Element] = Field(
        None, alias='_unit', description='Extensions for unit'
    )
    system: Optional[Uri] = Field(
        None,
        description='The identification of the system that provides the coded form of the unit.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    code: Optional[Code] = Field(
        None,
        description='A computer processable form of the unit in some unit representation system.',
    )
    field_code: Optional[Element] = Field(
        None, alias='_code', description='Extensions for code'
    )


class Range(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    low: Optional[Quantity] = Field(
        None, description='The low limit. The boundary is inclusive.'
    )
    high: Optional[Quantity] = Field(
        None, description='The high limit. The boundary is inclusive.'
    )


class Period(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    start: Optional[DateTime] = Field(
        None, description='The start of the period. The boundary is inclusive.'
    )
    field_start: Optional[Element] = Field(
        None, alias='_start', description='Extensions for start'
    )
    end: Optional[DateTime] = Field(
        None,
        description='The end of the period. If the end of the period is missing, it means no end was known or planned at the time the instance was created. The start may be in the past, and the end date in the future, which means that period is expected/planned to end at that time.',
    )
    field_end: Optional[Element] = Field(
        None, alias='_end', description='Extensions for end'
    )


class Ratio(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    numerator: Optional[Quantity] = Field(
        None, description='The value of the numerator.'
    )
    denominator: Optional[Quantity] = Field(
        None, description='The value of the denominator.'
    )


class RatioRange(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    lowNumerator: Optional[Quantity] = Field(
        None, description='The value of the low limit numerator.'
    )
    highNumerator: Optional[Quantity] = Field(
        None, description='The value of the high limit numerator.'
    )
    denominator: Optional[Quantity] = Field(
        None, description='The value of the denominator.'
    )


class Reference(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    reference: Optional[String] = Field(
        None,
        description="A reference to a location at which the other resource is found. The reference may be a relative reference, in which case it is relative to the service base URL, or an absolute URL that resolves to the location where the resource is found. The reference may be version specific or not. If the reference is not to a FHIR RESTful server, then it should be assumed to be version specific. Internal fragment references (start with '#') refer to contained resources.",
    )
    field_reference: Optional[Element] = Field(
        None, alias='_reference', description='Extensions for reference'
    )
    type: Optional[Uri] = Field(
        None,
        description='The expected type of the target of the reference. If both Reference.type and Reference.reference are populated and Reference.reference is a FHIR URL, both SHALL be consistent.\n\nThe type is the Canonical URL of Resource Definition that is the type this reference refers to. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only allowed for logical models (and can only be used in references in logical models, not resources).',
    )
    field_type: Optional[Element] = Field(
        None, alias='_type', description='Extensions for type'
    )
    identifier: Optional[Identifier] = Field(
        None,
        description='An identifier for the target resource. This is used when there is no way to reference the other resource directly, either because the entity it represents is not available through a FHIR server, or because there is no way for the author of the resource to convert a known identifier to an actual location. There is no requirement that a Reference.identifier point to something that is actually exposed as a FHIR instance, but it SHALL point to a business concept that would be expected to be exposed as a FHIR instance, and that instance would need to be of a FHIR resource type allowed by the reference.',
    )
    display: Optional[String] = Field(
        None,
        description='Plain text narrative that identifies the resource in addition to the resource reference.',
    )
    field_display: Optional[Element] = Field(
        None, alias='_display', description='Extensions for display'
    )


class SampledData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    origin: Quantity = Field(
        ...,
        description='The base quantity that a measured value of zero represents. In addition, this provides the units of the entire measurement series.',
    )
    interval: Optional[Decimal] = Field(
        None,
        description='Amount of intervalUnits between samples, e.g. milliseconds for time-based sampling.',
    )
    field_interval: Optional[Element] = Field(
        None, alias='_interval', description='Extensions for interval'
    )
    intervalUnit: Optional[Code] = Field(
        None,
        description='The measurement unit in which the sample interval is expressed.',
    )
    field_intervalUnit: Optional[Element] = Field(
        None, alias='_intervalUnit', description='Extensions for intervalUnit'
    )
    factor: Optional[Decimal] = Field(
        None,
        description='A correction factor that is applied to the sampled data points before they are added to the origin.',
    )
    field_factor: Optional[Element] = Field(
        None, alias='_factor', description='Extensions for factor'
    )
    lowerLimit: Optional[Decimal] = Field(
        None,
        description='The lower limit of detection of the measured points. This is needed if any of the data points have the value "L" (lower than detection limit).',
    )
    field_lowerLimit: Optional[Element] = Field(
        None, alias='_lowerLimit', description='Extensions for lowerLimit'
    )
    upperLimit: Optional[Decimal] = Field(
        None,
        description='The upper limit of detection of the measured points. This is needed if any of the data points have the value "U" (higher than detection limit).',
    )
    field_upperLimit: Optional[Element] = Field(
        None, alias='_upperLimit', description='Extensions for upperLimit'
    )
    dimensions: Optional[PositiveInt] = Field(
        None,
        description='The number of sample points at each time point. If this value is greater than one, then the dimensions will be interlaced - all the sample points for a point in time will be recorded at once.',
    )
    field_dimensions: Optional[Element] = Field(
        None, alias='_dimensions', description='Extensions for dimensions'
    )
    codeMap: Optional[Canonical] = Field(
        None,
        description='Reference to ConceptMap that defines the codes used in the data.',
    )
    offsets: Optional[String] = Field(
        None,
        description='A series of data points which are decimal values separated by a single space (character u20).  The units in which the offsets are expressed are found in intervalUnit.  The absolute point at which the measurements begin SHALL be conveyed outside the scope of this datatype, e.g. Observation.effectiveDateTime for a timing offset.',
    )
    field_offsets: Optional[Element] = Field(
        None, alias='_offsets', description='Extensions for offsets'
    )
    data: Optional[String] = Field(
        None,
        description='A series of data points which are decimal values or codes separated by a single space (character u20). The special codes "E" (error), "L" (below detection limit) and "U" (above detection limit) are also defined for used in place of decimal values.',
    )
    field_data: Optional[Element] = Field(
        None, alias='_data', description='Extensions for data'
    )


class Signature(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    type: Optional[List[Coding]] = Field(
        None,
        description='An indication of the reason that the entity signed this document. This may be explicitly included as part of the signature information and can be used when determining accountability for various actions concerning the document.',
    )
    when: Optional[Instant] = Field(
        None, description='When the digital signature was signed.'
    )
    field_when: Optional[Element] = Field(
        None, alias='_when', description='Extensions for when'
    )
    who: Optional[Reference] = Field(
        None,
        description='A reference to an application-usable description of the identity that signed  (e.g. the signature used their private key).',
    )
    onBehalfOf: Optional[Reference] = Field(
        None,
        description='A reference to an application-usable description of the identity that is represented by the signature.',
    )
    targetFormat: Optional[Code] = Field(
        None,
        description='A mime type that indicates the technical format of the target resources signed by the signature.',
    )
    field_targetFormat: Optional[Element] = Field(
        None, alias='_targetFormat', description='Extensions for targetFormat'
    )
    sigFormat: Optional[Code] = Field(
        None,
        description='A mime type that indicates the technical format of the signature. Important mime types are application/signature+xml for X ML DigSig, application/jose for JWS, and image/* for a graphical image of a signature, etc.',
    )
    field_sigFormat: Optional[Element] = Field(
        None, alias='_sigFormat', description='Extensions for sigFormat'
    )
    data: Optional[Base64Binary] = Field(
        None,
        description='The base64 encoding of the Signature content. When signature is not recorded electronically this element would be empty.',
    )
    field_data: Optional[Element] = Field(
        None, alias='_data', description='Extensions for data'
    )


class HumanName(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    use: Optional[Use1] = Field(
        None, description='Identifies the purpose for this name.'
    )
    field_use: Optional[Element] = Field(
        None, alias='_use', description='Extensions for use'
    )
    text: Optional[String] = Field(
        None,
        description='Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts.',
    )
    field_text: Optional[Element] = Field(
        None, alias='_text', description='Extensions for text'
    )
    family: Optional[String] = Field(
        None,
        description='The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father.',
    )
    field_family: Optional[Element] = Field(
        None, alias='_family', description='Extensions for family'
    )
    given: Optional[List[String]] = Field(None, description='Given name.')
    field_given: Optional[List[Element]] = Field(
        None, alias='_given', description='Extensions for given'
    )
    prefix: Optional[List[String]] = Field(
        None,
        description='Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name.',
    )
    field_prefix: Optional[List[Element]] = Field(
        None, alias='_prefix', description='Extensions for prefix'
    )
    suffix: Optional[List[String]] = Field(
        None,
        description='Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name.',
    )
    field_suffix: Optional[List[Element]] = Field(
        None, alias='_suffix', description='Extensions for suffix'
    )
    period: Optional[Period] = Field(
        None,
        description='Indicates the period of time when this name was valid for the named person.',
    )


class Address(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    use: Optional[Use2] = Field(None, description='The purpose of this address.')
    field_use: Optional[Element] = Field(
        None, alias='_use', description='Extensions for use'
    )
    type: Optional[Type] = Field(
        None,
        description='Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.',
    )
    field_type: Optional[Element] = Field(
        None, alias='_type', description='Extensions for type'
    )
    text: Optional[String] = Field(
        None,
        description='Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts.',
    )
    field_text: Optional[Element] = Field(
        None, alias='_text', description='Extensions for text'
    )
    line: Optional[List[String]] = Field(
        None,
        description='This component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address information.',
    )
    field_line: Optional[List[Element]] = Field(
        None, alias='_line', description='Extensions for line'
    )
    city: Optional[String] = Field(
        None,
        description='The name of the city, town, suburb, village or other community or delivery center.',
    )
    field_city: Optional[Element] = Field(
        None, alias='_city', description='Extensions for city'
    )
    district: Optional[String] = Field(
        None, description='The name of the administrative area (county).'
    )
    field_district: Optional[Element] = Field(
        None, alias='_district', description='Extensions for district'
    )
    state: Optional[String] = Field(
        None,
        description='Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes).',
    )
    field_state: Optional[Element] = Field(
        None, alias='_state', description='Extensions for state'
    )
    postalCode: Optional[String] = Field(
        None,
        description='A postal code designating a region defined by the postal service.',
    )
    field_postalCode: Optional[Element] = Field(
        None, alias='_postalCode', description='Extensions for postalCode'
    )
    country: Optional[String] = Field(
        None,
        description='Country - a nation as commonly understood or generally accepted.',
    )
    field_country: Optional[Element] = Field(
        None, alias='_country', description='Extensions for country'
    )
    period: Optional[Period] = Field(
        None, description='Time period when address was/is in use.'
    )


class ContactPoint(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    system: Optional[System] = Field(
        None,
        description='Telecommunications form for contact point - what communications system is required to make use of the contact.',
    )
    field_system: Optional[Element] = Field(
        None, alias='_system', description='Extensions for system'
    )
    value: Optional[String] = Field(
        None,
        description='The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address).',
    )
    field_value: Optional[Element] = Field(
        None, alias='_value', description='Extensions for value'
    )
    use: Optional[Use3] = Field(
        None, description='Identifies the purpose for the contact point.'
    )
    field_use: Optional[Element] = Field(
        None, alias='_use', description='Extensions for use'
    )
    rank: Optional[PositiveInt] = Field(
        None,
        description='Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values.',
    )
    field_rank: Optional[Element] = Field(
        None, alias='_rank', description='Extensions for rank'
    )
    period: Optional[Period] = Field(
        None, description='Time period when the contact point was/is in use.'
    )


class Timing(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.\n\nModifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    event: Optional[List[DateTime]] = Field(
        None, description='Identifies specific times when the event occurs.'
    )
    field_event: Optional[List[Element]] = Field(
        None, alias='_event', description='Extensions for event'
    )
    repeat: Optional[TimingRepeat] = Field(
        None, description='A set of rules that describe when the event is scheduled.'
    )
    code: Optional[CodeableConcept] = Field(
        None,
        description='A code for the timing schedule (or just text in code.text). Some codes such as BID are ubiquitous, but many institutions define their own additional codes. If a code is provided, the code is understood to be a complete statement of whatever is specified in the structured timing data, and either the code or the data may be used to interpret the Timing, with the exception that .repeat.bounds still applies over the code (and is not contained in the code).',
    )


class TimingRepeat(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    modifierExtension: Optional[List[Extension]] = Field(
        None,
        description="May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.\n\nModifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).",
    )
    boundsDuration: Optional[Duration] = Field(
        None,
        description='Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.',
    )
    boundsRange: Optional[Range] = Field(
        None,
        description='Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.',
    )
    boundsPeriod: Optional[Period] = Field(
        None,
        description='Either a duration for the length of the timing schedule, a range of possible length, or outer bounds for start and/or end limits of the timing schedule.',
    )
    count: Optional[PositiveInt] = Field(
        None,
        description='A total count of the desired number of repetitions across the duration of the entire timing specification. If countMax is present, this element indicates the lower bound of the allowed range of count values.',
    )
    field_count: Optional[Element] = Field(
        None, alias='_count', description='Extensions for count'
    )
    countMax: Optional[PositiveInt] = Field(
        None,
        description='If present, indicates that the count is a range - so to perform the action between [count] and [countMax] times.',
    )
    field_countMax: Optional[Element] = Field(
        None, alias='_countMax', description='Extensions for countMax'
    )
    duration: Optional[Decimal] = Field(
        None,
        description='How long this thing happens for when it happens. If durationMax is present, this element indicates the lower bound of the allowed range of the duration.',
    )
    field_duration: Optional[Element] = Field(
        None, alias='_duration', description='Extensions for duration'
    )
    durationMax: Optional[Decimal] = Field(
        None,
        description='If present, indicates that the duration is a range - so to perform the action between [duration] and [durationMax] time length.',
    )
    field_durationMax: Optional[Element] = Field(
        None, alias='_durationMax', description='Extensions for durationMax'
    )
    durationUnit: Optional[DurationUnit] = Field(
        None,
        description="The units of time for the duration, in UCUM units\nNormal practice is to use the 'mo' code as a calendar month when calculating the next occurrence.",
    )
    field_durationUnit: Optional[Element] = Field(
        None, alias='_durationUnit', description='Extensions for durationUnit'
    )
    frequency: Optional[PositiveInt] = Field(
        None,
        description='The number of times to repeat the action within the specified period. If frequencyMax is present, this element indicates the lower bound of the allowed range of the frequency.',
    )
    field_frequency: Optional[Element] = Field(
        None, alias='_frequency', description='Extensions for frequency'
    )
    frequencyMax: Optional[PositiveInt] = Field(
        None,
        description='If present, indicates that the frequency is a range - so to repeat between [frequency] and [frequencyMax] times within the period or period range.',
    )
    field_frequencyMax: Optional[Element] = Field(
        None, alias='_frequencyMax', description='Extensions for frequencyMax'
    )
    period: Optional[Decimal] = Field(
        None,
        description='Indicates the duration of time over which repetitions are to occur; e.g. to express "3 times per day", 3 would be the frequency and "1 day" would be the period. If periodMax is present, this element indicates the lower bound of the allowed range of the period length.',
    )
    field_period: Optional[Element] = Field(
        None, alias='_period', description='Extensions for period'
    )
    periodMax: Optional[Decimal] = Field(
        None,
        description='If present, indicates that the period is a range from [period] to [periodMax], allowing expressing concepts such as "do this once every 3-5 days.',
    )
    field_periodMax: Optional[Element] = Field(
        None, alias='_periodMax', description='Extensions for periodMax'
    )
    periodUnit: Optional[PeriodUnit] = Field(
        None,
        description="The units of time for the period in UCUM units\nNormal practice is to use the 'mo' code as a calendar month when calculating the next occurrence.",
    )
    field_periodUnit: Optional[Element] = Field(
        None, alias='_periodUnit', description='Extensions for periodUnit'
    )
    dayOfWeek: Optional[List[Code]] = Field(
        None,
        description='If one or more days of week is provided, then the action happens only on the specified day(s).',
    )
    field_dayOfWeek: Optional[List[Element]] = Field(
        None, alias='_dayOfWeek', description='Extensions for dayOfWeek'
    )
    timeOfDay: Optional[List[Time]] = Field(
        None, description='Specified time of day for action to take place.'
    )
    field_timeOfDay: Optional[List[Element]] = Field(
        None, alias='_timeOfDay', description='Extensions for timeOfDay'
    )
    when: Optional[List[WhenEnum]] = Field(
        None,
        description='An approximate time period during the day, potentially linked to an event of daily living that indicates when the action should occur.',
    )
    field_when: Optional[List[Element]] = Field(
        None, alias='_when', description='Extensions for when'
    )
    offset: Optional[UnsignedInt] = Field(
        None,
        description='The number of minutes from the event. If the event code does not indicate whether the minutes is before or after the event, then the offset is assumed to be after the event.',
    )
    field_offset: Optional[Element] = Field(
        None, alias='_offset', description='Extensions for offset'
    )


class Meta(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    versionId: Optional[Id] = Field(
        None,
        description='The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.',
    )
    field_versionId: Optional[Element] = Field(
        None, alias='_versionId', description='Extensions for versionId'
    )
    lastUpdated: Optional[Instant] = Field(
        None,
        description='When the resource last changed - e.g. when the version changed.',
    )
    field_lastUpdated: Optional[Element] = Field(
        None, alias='_lastUpdated', description='Extensions for lastUpdated'
    )
    source: Optional[Uri] = Field(
        None,
        description='A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.',
    )
    field_source: Optional[Element] = Field(
        None, alias='_source', description='Extensions for source'
    )
    profile: Optional[List[Canonical]] = Field(
        None,
        description='A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].',
    )
    security: Optional[List[Coding]] = Field(
        None,
        description='Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.',
    )
    tag: Optional[List[Coding]] = Field(
        None,
        description='Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.',
    )


class ContactDetail(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    name: Optional[String] = Field(
        None, description='The name of an individual to contact.'
    )
    field_name: Optional[Element] = Field(
        None, alias='_name', description='Extensions for name'
    )
    telecom: Optional[List[ContactPoint]] = Field(
        None,
        description='The contact details for the individual (if a name was provided) or the organization.',
    )


class Expression(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    description: Optional[String] = Field(
        None,
        description='A brief, natural language description of the condition that effectively communicates the intended semantics.',
    )
    field_description: Optional[Element] = Field(
        None, alias='_description', description='Extensions for description'
    )
    name: Optional[Code] = Field(
        None,
        description='A short name assigned to the expression to allow for multiple reuse of the expression in the context where it is defined.',
    )
    field_name: Optional[Element] = Field(
        None, alias='_name', description='Extensions for name'
    )
    language: Optional[Code] = Field(
        None, description='The media type of the language for the expression.'
    )
    field_language: Optional[Element] = Field(
        None, alias='_language', description='Extensions for language'
    )
    expression: Optional[String] = Field(
        None,
        description='An expression in the specified language that returns a value.',
    )
    field_expression: Optional[Element] = Field(
        None, alias='_expression', description='Extensions for expression'
    )
    reference: Optional[Uri] = Field(
        None, description='A URI that defines where the expression is found.'
    )
    field_reference: Optional[Element] = Field(
        None, alias='_reference', description='Extensions for reference'
    )

class ParameterDefinition(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    name: Optional[Code] = Field(
        None,
        description='The name of the parameter used to allow access to the value of the parameter in evaluation contexts.',
    )
    field_name: Optional[Element] = Field(
        None, alias='_name', description='Extensions for name'
    )
    use: Optional[Code] = Field(
        None, description='Whether the parameter is input or output for the module.'
    )
    field_use: Optional[Element] = Field(
        None, alias='_use', description='Extensions for use'
    )
    min: Optional[Integer] = Field(
        None,
        description='The minimum number of times this parameter SHALL appear in the request or response.',
    )
    field_min: Optional[Element] = Field(
        None, alias='_min', description='Extensions for min'
    )
    max: Optional[String] = Field(
        None,
        description='The maximum number of times this element is permitted to appear in the request or response.',
    )
    field_max: Optional[Element] = Field(
        None, alias='_max', description='Extensions for max'
    )
    documentation: Optional[String] = Field(
        None,
        description='A brief discussion of what the parameter is for and how it is used by the module.',
    )
    field_documentation: Optional[Element] = Field(
        None, alias='_documentation', description='Extensions for documentation'
    )
    type: Optional[Code] = Field(None, description='The type of the parameter.')
    field_type: Optional[Element] = Field(
        None, alias='_type', description='Extensions for type'
    )
    profile: Optional[Canonical] = Field(
        None,
        description='If specified, this indicates a profile that the input data must conform to, or that the output data will conform to.',
    )

class UsageContext(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[String] = Field(
        None,
        description='Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.',
    )
    extension: Optional[List[Extension]] = Field(
        None,
        description='May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and managable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.',
    )
    code: Coding = Field(
        ...,
        description='A code that identifies the type of context being specified by this usage context.',
    )
    valueCodeableConcept: Optional[CodeableConcept] = Field(
        None,
        description='A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.',
    )
    valueQuantity: Optional[Quantity] = Field(
        None,
        description='A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.',
    )
    valueRange: Optional[Range] = Field(
        None,
        description='A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.',
    )
    valueReference: Optional[Reference] = Field(
        None,
        description='A value that defines the context specified in this context of use. The interpretation of the value is defined by the code.',
    )
