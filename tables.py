# coding: utf-8

# this file was created by sqlacodegen using command:
# sqlacodegen postgresql://USERNAME:PASSWORD@pg_intsysd01_dev.bdns.bloomberg.com:4331/iappsgeod --schema contracts

from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#stupid hack for mypy
class Base(object):
    metadata: object

# don't remove the comment on the next line this is part of the mypy hack
Base = declarative_base() # type: ignore
metadata = Base.metadata


class Appendix(Base):
    __tablename__ = 'appendix'
    __table_args__ = {'schema': 'contracts'}

    appendix_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.appendix_appendix_id_seq'::regclass)"))
    title: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class BusinessDocType(Base):
    __tablename__ = 'business_doc_type'
    __table_args__ = {'schema': 'contracts'}

    business_doc_type_id: int = Column(Integer, primary_key=True)
    name: str = Column(Text, nullable=False)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    is_agreement: bool = Column(Boolean, nullable=False)
    bb_sign_applicable: bool = Column(Boolean, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class Clause(Base):
    __tablename__ = 'clause'
    __table_args__ = (
        UniqueConstraint('name', 'version'),
        {'schema': 'contracts'}
    )

    clause_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.clause_clause_id_seq'::regclass)"))
    name: str = Column(Text)
    version: int = Column(Integer, nullable=False)
    content: str = Column(Text, nullable=False)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class DatapointType(Base):
    __tablename__ = 'datapoint_type'
    __table_args__ = {'schema': 'contracts'}

    datapoint_type_id: int = Column(Integer, primary_key=True)
    name: str = Column(Text, nullable=False, unique=True)
    description: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class Language(Base):
    __tablename__ = 'language'
    __table_args__ = {'schema': 'contracts'}

    language_id: int = Column(Integer, primary_key=True)
    description: str = Column(Text, nullable=False, unique=True)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class LegalCategory(Base):
    __tablename__ = 'legal_category'
    __table_args__ = {'schema': 'contracts'}

    legal_category_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.legal_category_legal_category_id_seq'::regclass)"))
    name: str = Column(Text, nullable=False, unique=True)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    parent_legal_category_id: int = Column(ForeignKey('contracts.legal_category.legal_category_id'))
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    parent_legal_category = relationship('LegalCategory', remote_side=[legal_category_id])


class Section(Base):
    __tablename__ = 'section'
    __table_args__ = {'schema': 'contracts'}

    section_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.section_section_id_seq'::regclass)"))
    title: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class TemplateAttributeGroup(Base):
    __tablename__ = 'template_attribute_group'
    __table_args__ = {'schema': 'contracts'}

    template_attribute_group_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_attribute_group_template_attribute_group_id_seq'::regclass)"))
    name: str = Column(Text, nullable=False)
    title: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class TemplateTable(Base):
    __tablename__ = 'template_table'
    __table_args__ = {'schema': 'contracts'}

    template_table_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_table_template_table_id_seq'::regclass)"))
    name: str = Column(Text)
    title: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))


class BusinessDoc(Base):
    __tablename__ = 'business_doc'
    __table_args__ = {'schema': 'contracts'}

    business_doc_id: int = Column(Integer, primary_key=True)
    name: str = Column(Text, nullable=False)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    business_doc_type_id: int = Column(ForeignKey('contracts.business_doc_type.business_doc_type_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(DateTime, nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(DateTime)

    business_doc_type = relationship('BusinessDocType')


class ClauseDependency(Base):
    __tablename__ = 'clause_dependency'
    __table_args__ = {'schema': 'contracts'}

    clause_dependency_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.clause_dependency_clause_dependency_id_seq'::regclass)"))
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    dependent_on_clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    dependency_note: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause', primaryjoin='ClauseDependency.clause_id == Clause.clause_id')
    dependent_on_clause = relationship('Clause', primaryjoin='ClauseDependency.dependent_on_clause_id == Clause.clause_id')


class ClauseLegalCategoryLink(Base):
    __tablename__ = 'clause_legal_category_link'
    __table_args__ = {'schema': 'contracts'}

    clause_legal_category_link_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.clause_legal_category_link_clause_legal_category_link_id_seq'::regclass)"))
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    legal_category_id: int = Column(ForeignKey('contracts.legal_category.legal_category_id'), nullable=False)
    precedence: int = Column(Integer, nullable=False)
    obsolete: bool = Column(Boolean, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause')
    legal_category = relationship('LegalCategory')


class ClauseReference(Base):
    __tablename__ = 'clause_reference'
    __table_args__ = {'schema': 'contracts'}

    clause_reference_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.clause_reference_clause_reference_id_seq'::regclass)"))
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    referenced_clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    name: str = Column(Text, nullable=False)
    note: str = Column(Text)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause', primaryjoin='ClauseReference.clause_id == Clause.clause_id')
    referenced_clause = relationship('Clause', primaryjoin='ClauseReference.referenced_clause_id == Clause.clause_id')


class Datapoint(Base):
    __tablename__ = 'datapoint'
    __table_args__ = {'schema': 'contracts'}

    datapoint_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.datapoint_datapoint_id_seq'::regclass)"))
    name: str = Column(Text, nullable=False, unique=True)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    type_id: int = Column(ForeignKey('contracts.datapoint_type.datapoint_type_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    type = relationship('DatapointType')


class Paragraph(Base):
    __tablename__ = 'paragraph'
    __table_args__ = {'schema': 'contracts'}

    paragraph_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.paragraph_paragraph_id_seq'::regclass)"))
    section_id: int = Column(ForeignKey('contracts.section.section_id'), nullable=False)
    name: int = Column(Text)
    sequence: int = Column(Integer, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    section = relationship('Section')


class TemplateTableRow(Base):
    __tablename__ = 'template_table_row'
    __table_args__ = {'schema': 'contracts'}

    template_table_row_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_table_row_template_table_row_id_seq'::regclass)"))
    is_header: bool = Column(Boolean, nullable=False)
    sequence: int = Column(Integer, nullable=False)
    template_table_id: int = Column(ForeignKey('contracts.template_table.template_table_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    template_table = relationship('TemplateTable')


class ClauseDatapointLink(Base):
    __tablename__ = 'clause_datapoint_link'
    __table_args__ = {'schema': 'contracts'}

    clause_datapoint_link_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.clause_datapoint_link_clause_datapoint_link_id_seq'::regclass)"))
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    datapoint_id: int = Column(ForeignKey('contracts.datapoint.datapoint_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause')
    datapoint = relationship('Datapoint')


class ParagraphClauseLink(Base):
    __tablename__ = 'paragraph_clause_link'
    __table_args__ = {'schema': 'contracts'}

    paragraph_clause_link_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.paragraph_clause_link_paragraph_clause_link_id_seq'::regclass)"))
    paragraph_id: int = Column(ForeignKey('contracts.paragraph.paragraph_id'), nullable=False)
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    sequence: int = Column(Integer, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause')
    paragraph = relationship('Paragraph')


class SpecialLanguage(Base):
    __tablename__ = 'special_language'
    __table_args__ = {'schema': 'contracts'}

    special_language_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.special_language_special_language_id_seq'::regclass)"))
    datapoint_id: int = Column(ForeignKey('contracts.datapoint.datapoint_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    datapoint = relationship('Datapoint')


class Template(Base):
    __tablename__ = 'template'
    __table_args__ = (
        UniqueConstraint('version', 'name'),
        {'schema': 'contracts'}
    )

    template_id: int = Column(Integer, primary_key=True)
    version: int = Column(Integer, nullable=False)
    name: str = Column(Text, nullable=False)
    business_doc_id: int = Column(ForeignKey('contracts.business_doc.business_doc_id'), nullable=False)
    language_id: int = Column(ForeignKey('contracts.language.language_id'), nullable=False)
    obsolete: bool = Column(Boolean, nullable=False, server_default=text("false"))
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    business_doc = relationship('BusinessDoc')
    language = relationship('Language')


class TemplateAttribute(Base):
    __tablename__ = 'template_attribute'
    __table_args__ = {'schema': 'contracts'}

    template_attribute_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_attribute_template_attribute_id_seq'::regclass)"))
    label: str = Column(Text)
    datapoint_id: int = Column(ForeignKey('contracts.datapoint.datapoint_id'), nullable=False)
    template_attribute_group_id: int = Column(ForeignKey('contracts.template_attribute_group.template_attribute_group_id'), nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))
    attribute_sequence: int = Column(Integer, nullable=False)

    datapoint = relationship('Datapoint')
    template_attribute_group = relationship('TemplateAttributeGroup')


class TemplateTableCell(Base):
    __tablename__ = 'template_table_cell'
    __table_args__ = {'schema': 'contracts'}

    template_table_cell_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_table_cell_template_table_cell_id_seq'::regclass)"))
    name: str = Column(Text)
    content: str = Column(Text)
    sequence: int = Column(Integer, nullable=False)
    template_table_row_id: int = Column(ForeignKey('contracts.template_table_row.template_table_row_id'), nullable=False)
    subtable_id: int = Column(ForeignKey('contracts.template_table.template_table_id'))
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    subtable = relationship('TemplateTable')
    template_table_row = relationship('TemplateTableRow')


class NegotiationStrategy(Base):
    __tablename__ = 'negotiation_strategy'
    __table_args__ = {'schema': 'contracts'}

    negotiation_strategy_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.negotiation_strategy_negotiation_strategy_id_seq'::regclass)"))
    template_id: int = Column(ForeignKey('contracts.template.template_id'), nullable=False)
    paragraph_id: int = Column(ForeignKey('contracts.paragraph.paragraph_id'), nullable=False)
    clause_id: int = Column(ForeignKey('contracts.clause.clause_id'), nullable=False)
    content: str = Column(Text, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    clause = relationship('Clause')
    paragraph = relationship('Paragraph')
    template = relationship('Template')


class Region(Base):
    __tablename__ = 'region'
    __table_args__ = {'schema': 'contracts'}

    region_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.region_region_id_seq'::regclass)"))
    template_id: int = Column(ForeignKey('contracts.template.template_id'))
    parent_region_id: int = Column(ForeignKey('contracts.region.region_id'))
    section_id: int = Column(ForeignKey('contracts.section.section_id'))
    template_attribute_group_id: int = Column(ForeignKey('contracts.template_attribute_group.template_attribute_group_id'))
    template_table_id: int = Column(Integer)
    special_language_id: int = Column(Integer)
    appendix_id: int = Column(ForeignKey('contracts.appendix.appendix_id'))
    sequence: int = Column(Integer, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    appendix = relationship('Appendix')
    parent_region = relationship('Region', remote_side=[region_id])
    section = relationship('Section')
    template_attribute_group = relationship('TemplateAttributeGroup')
    template = relationship('Template')


class TemplateTableCellDatapointLink(Base):
    __tablename__ = 'template_table_cell_datapoint_link'
    __table_args__ = {'schema': 'contracts'}

    template_table_cell_datapoint_link_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.template_table_cell_datapoint_template_table_cell_datapoint_seq'::regclass)"))
    template_table_cell_id: int = Column(ForeignKey('contracts.template_table_cell.template_table_cell_id'), nullable=False)
    datapoint_id: int = Column(ForeignKey('contracts.datapoint.datapoint_id'), nullable=False)
    sequence: int = Column(Integer, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    datapoint = relationship('Datapoint')
    template_table_cell = relationship('TemplateTableCell')


class StandardModification(Base):
    __tablename__ = 'standard_modification'
    __table_args__ = {'schema': 'contracts'}

    standard_modification_id: int = Column(Integer, primary_key=True, server_default=text("nextval('contracts.standard_modification_standard_modification_id_seq'::regclass)"))
    negotiation_strategy_id: int = Column(ForeignKey('contracts.negotiation_strategy.negotiation_strategy_id'), nullable=False)
    content: str = Column(Text, nullable=False)
    obsolete: bool = Column(Boolean, nullable=False)
    create_uuid: int = Column(Integer, nullable=False)
    create_timestamp_utc: datetime = Column(TIMESTAMP(True, 6), nullable=False)
    update_uuid: int = Column(Integer)
    update_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))
    approved_uuid: int = Column(Integer)
    approved_timestamp_utc: datetime = Column(TIMESTAMP(True, 6))

    negotiation_strategy = relationship('NegotiationStrategy')


