from odoo import api, fields, models

BURKINA_FASO_REGIONS = [
    ("boucle_du_mouhoun", "Boucle du Mouhoun"),
    ("cascades", "Cascades"),
    ("centre", "Centre"),
    ("centre_est", "Centre-Est"),
    ("centre_nord", "Centre-Nord"),
    ("centre_ouest", "Centre-Ouest"),
    ("centre_sud", "Centre-Sud"),
    ("est", "Est"),
    ("hauts_bassins", "Hauts-Bassins"),
    ("nord", "Nord"),
    ("plateau_central", "Plateau-Central"),
    ("sahel", "Sahel"),
    ("sud_ouest", "Sud-Ouest"),
    ("hors_burkina", "Hors Burkina Faso"),
]


class CrmLead(models.Model):
    _inherit = "crm.lead"

    activity_pole = fields.Selection(
        selection=[
            ("services_it", "Services digitaux & IT"),
            ("formation", "Formations IT"),
            ("equipement", "Vente d'équipements"),
        ],
        string="Pôle d'activité",
        tracking=True,
        help="Pôle d'activité Box Africa concerné par cette opportunité.",
    )
    region = fields.Selection(
        selection=BURKINA_FASO_REGIONS,
        string="Région",
        tracking=True,
    )
    client_type = fields.Selection(
        selection=[
            ("particulier", "Particulier"),
            ("pme", "PME"),
            ("grande_entreprise", "Grande entreprise"),
            ("administration", "Administration publique"),
            ("ong", "ONG / Organisation internationale"),
        ],
        string="Type de client",
        tracking=True,
    )

    # --- Pôle Services digitaux & IT -------------------------------------
    service_type = fields.Selection(
        selection=[
            ("dev_web", "Développement web"),
            ("dev_mobile", "Développement mobile"),
            ("infogerance", "Infogérance"),
            ("conseil_si", "Conseil en systèmes d'information"),
            ("hebergement", "Hébergement"),
            ("cybersecurite", "Cybersécurité"),
            ("integration", "Intégration de solutions logicielles"),
        ],
        string="Type de service IT",
    )
    service_urgency = fields.Selection(
        selection=[
            ("faible", "Faible"),
            ("normale", "Normale"),
            ("elevee", "Élevée"),
            ("critique", "Critique"),
        ],
        string="Urgence",
        default="normale",
    )

    # --- Pôle Formations IT ------------------------------------------------
    formation_type = fields.Selection(
        selection=[
            ("bureautique", "Bureautique"),
            ("developpement", "Développement"),
            ("reseaux", "Réseaux"),
            ("cybersecurite", "Cybersécurité"),
            ("certification", "Préparation aux certifications"),
        ],
        string="Type de formation",
    )
    formation_modality = fields.Selection(
        selection=[
            ("presentiel", "Présentiel"),
            ("distance", "À distance"),
            ("hybride", "Hybride"),
        ],
        string="Modalité",
    )
    formation_public = fields.Selection(
        selection=[
            ("particulier", "Particuliers"),
            ("entreprise", "Entreprises"),
        ],
        string="Public visé",
    )
    formation_participants = fields.Integer(string="Nombre de participants")
    formation_date = fields.Date(string="Date de session souhaitée")

    # --- Pôle Vente d'équipements -------------------------------------------
    equipment_category = fields.Selection(
        selection=[
            ("ordinateurs", "Ordinateurs"),
            ("serveurs", "Serveurs"),
            ("materiel_reseau", "Matériel réseau"),
            ("peripheriques", "Périphériques"),
            ("consommables", "Consommables"),
        ],
        string="Catégorie de matériel",
    )
    equipment_quantity = fields.Integer(string="Quantité estimée")
    equipment_installation = fields.Boolean(string="Installation requise")
    equipment_maintenance = fields.Boolean(string="Maintenance requise")

    @api.onchange("team_id")
    def _onchange_team_id_set_activity_pole(self):
        """Pré-remplit le pôle d'activité à partir de l'équipe commerciale
        choisie, pour éviter la ressaisie."""
        team_pole_map = {
            "box_africa_crm.crm_team_services_it": "services_it",
            "box_africa_crm.crm_team_formation": "formation",
            "box_africa_crm.crm_team_equipement": "equipement",
        }
        for xml_id, pole in team_pole_map.items():
            team = self.env.ref(xml_id, raise_if_not_found=False)
            if team and self.team_id == team:
                self.activity_pole = pole
                break
