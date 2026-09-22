{
    "name": "Box Africa CRM",
    "version": "19.0.1.0.0",
    "summary": "CRM adapté aux 3 pôles d'activité de Box Africa "
                "(Services digitaux & IT, Formations IT, Vente d'équipements)",
    "description": """
Box Africa CRM
===============
Personnalisation du CRM Odoo pour Box Africa (Ouagadougou, Burkina Faso) :

* Trois équipes commerciales dédiées : Services digitaux & IT, Formations IT,
  Vente d'équipements informatiques.
* Pipelines (étapes) propres à chaque pôle d'activité.
* Champs métier spécifiques par pôle sur les leads/opportunités.
* Champs communs : région (Burkina Faso) et type de client.
    """,
    "author": "Box Africa",
    "website": "https://boxafrica.bf",
    "category": "Sales/CRM",
    "license": "LGPL-3",
    "depends": ["crm"],
    "data": [
        "data/crm_team_data.xml",
        "data/crm_stage_data.xml",
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "application": False,
}
