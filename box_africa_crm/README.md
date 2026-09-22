# Box Africa CRM

Personnalisation du CRM Odoo pour les trois pôles d'activité de Box Africa.

## Ce que le module installe

- **3 équipes commerciales** (`crm.team`) : Services digitaux & IT,
  Formations IT, Vente d'équipements.
- **15 étapes de pipeline** (`crm.stage`, préfixées par pôle : "Services IT -
  ...", "Formation - ...", "Équipements - ...") adaptées au cycle de vente
  de chaque pôle. *Note : `crm.stage` n'a pas de champ de restriction par
  équipe dans cette version d'Odoo, donc les étapes sont partagées entre
  les 3 équipes (d'où le préfixe pour s'y retrouver).*
- **Champs sur les leads/opportunités** (`crm.lead`) :
  - Communs : `activity_pole` (pôle d'activité), `region` (région du
    Burkina Faso), `client_type`.
  - Services IT : `service_type`, `service_urgency`.
  - Formations : `formation_type`, `formation_modality`,
    `formation_public`, `formation_participants`, `formation_date`.
  - Équipements : `equipment_category`, `equipment_quantity`,
    `equipment_installation`, `equipment_maintenance`.
- Un onglet **"Box Africa"** dans le formulaire d'opportunité affiche les
  champs pertinents selon le pôle sélectionné.
- Le pôle d'activité se pré-remplit automatiquement quand on choisit
  l'équipe commerciale.

## Prochaines étapes possibles

- Colonnes/filtres/regroupements par pôle dans les vues liste et kanban.
- Tableaux de bord (vues pivot/graph) par pôle avec KPI (CA par pôle,
  taux de conversion, délai moyen de clôture).
- Intégrations externes (site web, WhatsApp Business, facturation) —
  à définir selon les outils utilisés par Box Africa.
- Règles d'assignation automatique des leads vers la bonne équipe selon
  le formulaire d'origine (site web, appel, etc.).

## Installation

Le module est détecté automatiquement par Odoo.sh (dossier à la racine du
dépôt avec un `__manifest__.py`). Après déploiement du build, l'installer
depuis **Apps > Mettre à jour la liste des applications**, puis rechercher
« Box Africa CRM ».

En local (odoo-bin) :

```bash
odoo-bin -d <db> -i box_africa_crm --addons-path=addons,box_africa_crm
```
