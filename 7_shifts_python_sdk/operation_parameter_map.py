operation_parameter_map = {
    '/v2/partner_company_creation-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'firstname'
            },
            {
                'name': 'lastname'
            },
            {
                'name': 'company_name'
            },
            {
                'name': 'country'
            },
            {
                'name': 'utm_source'
            },
            {
                'name': 'mobile_phone'
            },
            {
                'name': 'utm_campaign'
            },
            {
                'name': 'utm_content'
            },
            {
                'name': 'utm_medium'
            },
            {
                'name': 'utm_term'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/oauth2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/v2/whoami-GET': {
        'parameters': [
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'repeat'
            },
            {
                'name': 'mon'
            },
            {
                'name': 'mon_from'
            },
            {
                'name': 'mon_to'
            },
            {
                'name': 'mon_comments'
            },
            {
                'name': 'mon_reason'
            },
            {
                'name': 'tue'
            },
            {
                'name': 'tue_from'
            },
            {
                'name': 'tue_to'
            },
            {
                'name': 'tue_comments'
            },
            {
                'name': 'tue_reason'
            },
            {
                'name': 'wed'
            },
            {
                'name': 'wed_from'
            },
            {
                'name': 'wed_to'
            },
            {
                'name': 'wed_comments'
            },
            {
                'name': 'wed_reason'
            },
            {
                'name': 'thu'
            },
            {
                'name': 'thu_from'
            },
            {
                'name': 'thu_to'
            },
            {
                'name': 'thu_comments'
            },
            {
                'name': 'thu_reason'
            },
            {
                'name': 'fri'
            },
            {
                'name': 'fri_from'
            },
            {
                'name': 'fri_to'
            },
            {
                'name': 'fri_comments'
            },
            {
                'name': 'fri_reason'
            },
            {
                'name': 'sat'
            },
            {
                'name': 'sat_from'
            },
            {
                'name': 'sat_to'
            },
            {
                'name': 'sat_comments'
            },
            {
                'name': 'sat_reason'
            },
            {
                'name': 'sun'
            },
            {
                'name': 'sun_from'
            },
            {
                'name': 'sun_to'
            },
            {
                'name': 'sun_comments'
            },
            {
                'name': 'sun_reason'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'week'
            },
            {
                'name': 'week_to'
            },
        ]
    },
    '/v2/company/{company_id}/availability_reasons-POST': {
        'parameters': [
            {
                'name': 'reason'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'comments_required'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/availability_reasons/{availability_reason_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_reason_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities/{availability_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_id'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'repeating'
            },
            {
                'name': 'week_gte'
            },
            {
                'name': 'week_to_include_repeating_gte'
            },
            {
                'name': 'order_field'
            },
            {
                'name': 'order_dir'
            },
        ]
    },
    '/v2/company/{company_id}/availability_reasons-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities/{availability_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_id'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities/{availability_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_id'
            },
            {
                'name': 'week'
            },
            {
                'name': 'week_to'
            },
            {
                'name': 'repeat'
            },
            {
                'name': 'mon'
            },
            {
                'name': 'mon_from'
            },
            {
                'name': 'mon_to'
            },
            {
                'name': 'mon_comments'
            },
            {
                'name': 'mon_reason'
            },
            {
                'name': 'tue'
            },
            {
                'name': 'tue_from'
            },
            {
                'name': 'tue_to'
            },
            {
                'name': 'tue_comments'
            },
            {
                'name': 'tue_reason'
            },
            {
                'name': 'wed'
            },
            {
                'name': 'wed_from'
            },
            {
                'name': 'wed_to'
            },
            {
                'name': 'wed_comments'
            },
            {
                'name': 'wed_reason'
            },
            {
                'name': 'thu'
            },
            {
                'name': 'thu_from'
            },
            {
                'name': 'thu_to'
            },
            {
                'name': 'thu_comments'
            },
            {
                'name': 'thu_reason'
            },
            {
                'name': 'fri'
            },
            {
                'name': 'fri_from'
            },
            {
                'name': 'fri_to'
            },
            {
                'name': 'fri_comments'
            },
            {
                'name': 'fri_reason'
            },
            {
                'name': 'sat'
            },
            {
                'name': 'sat_from'
            },
            {
                'name': 'sat_to'
            },
            {
                'name': 'sat_comments'
            },
            {
                'name': 'sat_reason'
            },
            {
                'name': 'sun'
            },
            {
                'name': 'sun_from'
            },
            {
                'name': 'sun_to'
            },
            {
                'name': 'sun_comments'
            },
            {
                'name': 'sun_reason'
            },
        ]
    },
    '/v2/company/{company_id}/availability_reasons/{availability_reason_id}-PUT': {
        'parameters': [
            {
                'name': 'reason'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_reason_id'
            },
            {
                'name': 'comments_required'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/availabilities/{availability_id}/status-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'availability_id'
            },
            {
                'name': 'message'
            },
        ]
    },
    '/v2/companies/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/labor_settings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/companies-GET': {
        'parameters': [
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'modified_since'
            },
        ]
    },
    '/v2/company/{company_id}/inactive_reasons-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/companies/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'country'
            },
            {
                'name': 'photo'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/day_part/settings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/departments-POST': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'default'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/departments/{department_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'transfer_to'
            },
        ]
    },
    '/v2/company/{company_id}/departments/{department_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/departments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/departments/{department_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'default'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/engage_overview-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'user_type'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings_bulk-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings/{identifier}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings/{identifier}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/external_user_mappings/{identifier}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/forecast_overrides-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/forecast_overrides_intervals-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/forecast_override-POST': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'value'
            },
            {
                'name': 'report_type'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/forecast_override_interval-POST': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'value'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'report_type'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/forecast_override-DELETE': {
        'parameters': [
            {
                'name': 'start_date'
            },
            {
                'name': 'report_type'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/forecast_override_interval-DELETE': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'report_type'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/sales_category_mappings_bulk-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/sales_category_mappings/{external_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/location/{location_id}/sales_category_mappings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/locations-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'country'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'formatted_address'
            },
            {
                'name': 'state'
            },
            {
                'name': 'city'
            },
            {
                'name': 'latitude'
            },
            {
                'name': 'longitude'
            },
            {
                'name': 'place_id'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'holiday_pay'
            },
            {
                'name': 'sun_hours_close'
            },
            {
                'name': 'mon_hours_close'
            },
            {
                'name': 'tue_hours_close'
            },
            {
                'name': 'wed_hours_close'
            },
            {
                'name': 'thu_hours_close'
            },
            {
                'name': 'fri_hours_close'
            },
            {
                'name': 'sat_hours_close'
            },
            {
                'name': 'sun_hours_open'
            },
            {
                'name': 'mon_hours_open'
            },
            {
                'name': 'tue_hours_open'
            },
            {
                'name': 'wed_hours_open'
            },
            {
                'name': 'thu_hours_open'
            },
            {
                'name': 'fri_hours_open'
            },
            {
                'name': 'sat_hours_open'
            },
            {
                'name': 'sun_is_closed'
            },
            {
                'name': 'mon_is_closed'
            },
            {
                'name': 'tue_is_closed'
            },
            {
                'name': 'wed_is_closed'
            },
            {
                'name': 'thu_is_closed'
            },
            {
                'name': 'fri_is_closed'
            },
            {
                'name': 'sat_is_closed'
            },
            {
                'name': 'enable_shift_feedback'
            },
            {
                'name': 'shift_feedback'
            },
            {
                'name': 'coupon'
            },
            {
                'name': 'stripe_token_id'
            },
            {
                'name': 'copy_from_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'deleted'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
            {
                'name': 'state'
            },
            {
                'name': 'shift_feedback'
            },
            {
                'name': 'formatted_address'
            },
            {
                'name': 'lat'
            },
            {
                'name': 'lng'
            },
            {
                'name': 'place_id'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'hash'
            },
            {
                'name': 'department_based_budget'
            },
            {
                'name': 'holiday_pay'
            },
            {
                'name': 'auto_send_log_book_time'
            },
            {
                'name': 'sun_hours_close'
            },
            {
                'name': 'mon_hours_close'
            },
            {
                'name': 'tue_hours_close'
            },
            {
                'name': 'wed_hours_close'
            },
            {
                'name': 'thu_hours_close'
            },
            {
                'name': 'fri_hours_close'
            },
            {
                'name': 'sat_hours_close'
            },
            {
                'name': 'sun_hours_open'
            },
            {
                'name': 'mon_hours_open'
            },
            {
                'name': 'tue_hours_open'
            },
            {
                'name': 'wed_hours_open'
            },
            {
                'name': 'thu_hours_open'
            },
            {
                'name': 'fri_hours_open'
            },
            {
                'name': 'sat_hours_open'
            },
            {
                'name': 'sun_is_closed'
            },
            {
                'name': 'mon_is_closed'
            },
            {
                'name': 'tue_is_closed'
            },
            {
                'name': 'wed_is_closed'
            },
            {
                'name': 'thu_is_closed'
            },
            {
                'name': 'fri_is_closed'
            },
            {
                'name': 'sat_is_closed'
            },
            {
                'name': 'message'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_categories-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'col'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'field_type'
            },
            {
                'name': 'notify'
            },
            {
                'name': 'required'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_comments-POST': {
        'parameters': [
            {
                'name': 'log_book_id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_posts-POST': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'log_book_category_id'
            },
            {
                'name': 'date'
            },
            {
                'name': 'message'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_categories/{id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_comments/{id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_posts/{id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_comments/{id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_posts/{id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_categories-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_comments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'log_book_ids'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_posts-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'log_book_category_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'date'
            },
            {
                'name': 'posted_date_gte'
            },
            {
                'name': 'posted_date_lte'
            },
            {
                'name': 'message'
            },
            {
                'name': 'order_field'
            },
            {
                'name': 'order_dir'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/log_book_categories/{id}-PATCH': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'col'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'field_type'
            },
            {
                'name': 'notify'
            },
            {
                'name': 'required'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/receipts-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'receipt_date'
            },
            {
                'name': 'net_total'
            },
            {
                'name': 'gross_total'
            },
            {
                'name': 'total_receipt_discounts'
            },
            {
                'name': 'tips'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'revenue_center'
            },
            {
                'name': 'receipt_lines'
            },
            {
                'name': 'tip_details'
            },
            {
                'name': 'status'
            },
            {
                'name': 'order_type'
            },
            {
                'name': 'dining_option'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/receipts/{receipt_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'receipt_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/receipts_summary-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'receipt_date[gte]'
            },
            {
                'name': 'receipt_date[lte]'
            },
            {
                'name': 'modified_since'
            },
        ]
    },
    '/v2/company/{company_id}/receipts-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'receipt_date[gte]'
            },
            {
                'name': 'receipt_date[lte]'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'status'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/receipts/{receipt_id}-PUT': {
        'parameters': [
            {
                'name': 'net_total'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'receipt_id'
            },
            {
                'name': 'receipt_date'
            },
            {
                'name': 'gross_total'
            },
            {
                'name': 'total_receipt_discounts'
            },
            {
                'name': 'tips'
            },
            {
                'name': 'external_user_id'
            },
            {
                'name': 'revenue_center'
            },
            {
                'name': 'receipt_lines'
            },
            {
                'name': 'tip_details'
            },
            {
                'name': 'status'
            },
            {
                'name': 'order_type'
            },
            {
                'name': 'dining_option'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/reports/daily_sales_and_labor-GET': {
        'parameters': [
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'department_id'
            },
        ]
    },
    '/api/v2/company/{company_id}/location/{location_id}/daily_stats-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'include_future'
            },
        ]
    },
    '/v2/reports/hours_and_wages-GET': {
        'parameters': [
            {
                'name': 'punches'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/company/{company_id}/roles-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'job_code'
            },
            {
                'name': 'stations'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/roles/{role_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/roles/{role_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/roles-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/roles/{role_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'color'
            },
            {
                'name': 'name'
            },
            {
                'name': 'job_code'
            },
            {
                'name': 'stations'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/shifts_scheduled/{id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'grace_period'
            },
        ]
    },
    '/v2/company/{company_id}/events-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'location_ids'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'is_multi_day'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'color'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/events/{event_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'event_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'recurrence_target'
            },
            {
                'name': 'start_date'
            },
        ]
    },
    '/v2/company/{company_id}/events/{event_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'event_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/events-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
        ]
    },
    '/v2/company/{company_id}/events/{event_id}-PATCH': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'event_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'location_ids'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'color'
            },
            {
                'name': 'is_multi_day'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'recurrence_target'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/shift_feedback-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/shifts-POST': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'station_id'
            },
            {
                'name': 'close'
            },
            {
                'name': 'business_decline'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'notified'
            },
            {
                'name': 'open'
            },
            {
                'name': 'open_offer_type'
            },
            {
                'name': 'unassigned'
            },
            {
                'name': 'unassigned_skill_level'
            },
            {
                'name': 'status'
            },
            {
                'name': 'late_minutes'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/shifts/{shift_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'shift_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/shifts/{shift_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'shift_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'include_deleted'
            },
        ]
    },
    '/v2/company/{company_id}/shifts-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'shift_ids'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'department_ids'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'start[lte]'
            },
            {
                'name': 'start[gte]'
            },
            {
                'name': 'end[lte]'
            },
            {
                'name': 'end[gte]'
            },
            {
                'name': 'deleted'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'include_draft'
            },
            {
                'name': 'open'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_dir'
            },
        ]
    },
    '/v2/company/{company_id}/shifts/{shift_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'shift_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'station_id'
            },
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'close'
            },
            {
                'name': 'business_decline'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'open'
            },
            {
                'name': 'open_offer_type'
            },
            {
                'name': 'unassigned'
            },
            {
                'name': 'unassigned_skill_level'
            },
            {
                'name': 'status'
            },
            {
                'name': 'late_minutes'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/clear-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_templates-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'assignments'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'due'
            },
            {
                'name': 'time_frame'
            },
            {
                'name': 'task_templates'
            },
            {
                'name': 'status'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_tags-POST': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_templates/{uuid}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'uuid'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_tags-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'uuids'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_templates/{uuid}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'uuid'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'status'
            },
            {
                'name': 'task_templates'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'assignments'
            },
            {
                'name': 'due'
            },
            {
                'name': 'time_frame'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/task_management_settings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
        ]
    },
    '/v2/company/{company_id}/task_lists/{list_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_templates/{uuid}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'uuid'
            },
            {
                'name': 'x-api-version'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_templates-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/task_lists-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'uuid'
            },
            {
                'name': 'active_on_date'
            },
        ]
    },
    '/v2/company/{company_id}/task_list_daily_summary-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/complete-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'completion_value'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off/{time_off_id}/approve-POST': {
        'parameters': [
            {
                'name': 'time_off_id'
            },
            {
                'name': 'status_action_message'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'from_date'
            },
            {
                'name': 'to_date'
            },
            {
                'name': 'partial'
            },
            {
                'name': 'status'
            },
            {
                'name': 'category'
            },
            {
                'name': 'partial_from'
            },
            {
                'name': 'partial_to'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'status_action_user_id'
            },
            {
                'name': 'status_action_message'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off/{time_off_id}/decline-POST': {
        'parameters': [
            {
                'name': 'time_off_id'
            },
            {
                'name': 'status_action_message'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off_settings/{company_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off/{time_off_id}-GET': {
        'parameters': [
            {
                'name': 'time_off_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off/total_hours-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'date_start'
            },
            {
                'name': 'date_end'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'category'
            },
            {
                'name': 'to_date_gte'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_dir'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/time_off/{time_off_id}-DELETE': {
        'parameters': [
            {
                'name': 'time_off_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/time_off_settings/{company_id}-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'paid_time_off'
            },
            {
                'name': 'sick_time_off'
            },
            {
                'name': 'time_off_request_comment'
            },
            {
                'name': 'time_off_request_notice'
            },
        ]
    },
    '/v2/time_off/{time_off_id}-PATCH': {
        'parameters': [
            {
                'name': 'time_off_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'from_date'
            },
            {
                'name': 'to_date'
            },
            {
                'name': 'partial'
            },
            {
                'name': 'partial_from'
            },
            {
                'name': 'partial_to'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'status'
            },
            {
                'name': 'status_action_message'
            },
            {
                'name': 'category'
            },
            {
                'name': 'hours'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/time_punches-POST': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'clocked_in'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'clocked_out'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'tips'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/time_punches/{time_punch_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'time_punch_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/time_punches/{time_punch_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'time_punch_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/time_punches-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'approved'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'clocked_in[lte]'
            },
            {
                'name': 'clocked_in[gte]'
            },
            {
                'name': 'clocked_out[lte]'
            },
            {
                'name': 'clocked_out[gte]'
            },
            {
                'name': 'include_deleted'
            },
            {
                'name': 'deleted'
            },
            {
                'name': 'localize_search_time'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/v2/company/{company_id}/time_punches/{time_punch_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'time_punch_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'clocked_in'
            },
            {
                'name': 'clocked_out'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'tips'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/tip_pool_detailed_report-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'tip_pool_uuid'
            },
            {
                'name': 'day_part_uuid'
            },
        ]
    },
    '/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'tip_pool_settings_uuid'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/tip_pool_settings-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/locations/{location_id}/tip_pool_summary_report-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'tip_pool_uuid'
            },
            {
                'name': 'day_part_uuid'
            },
        ]
    },
    '/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry-PUT': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'tip_pool_settings_uuid'
            },
            {
                'name': 'object'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/department_assignments-POST': {
        'parameters': [
            {
                'name': 'department_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'appear_on_schedule'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/location_assignments-POST': {
        'parameters': [
            {
                'name': 'location_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/role_assignments-POST': {
        'parameters': [
            {
                'name': 'role_id'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'primary'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/role_assignments/{role_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/department_assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/location_assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/role_assignments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/department_assignments/{department_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/location_assignments/{location_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/wages-POST': {
        'parameters': [
            {
                'name': 'effective_date'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'wage_cents'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{user_id}/wages-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/create_many_users-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'location_ids'
            },
            {
                'name': 'department_ids'
            },
            {
                'name': 'type'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'preferred_first_name'
            },
            {
                'name': 'preferred_last_name'
            },
            {
                'name': 'role_ids'
            },
            {
                'name': 'email'
            },
            {
                'name': 'mobile_number'
            },
            {
                'name': 'home_number'
            },
            {
                'name': 'address'
            },
            {
                'name': 'postal_zip'
            },
            {
                'name': 'city'
            },
            {
                'name': 'prov_state'
            },
            {
                'name': 'invite_user'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'punch_id'
            },
            {
                'name': 'birth_date'
            },
            {
                'name': 'language'
            },
            {
                'name': 'appear_as_employee'
            },
            {
                'name': 'subscribe_to_updates'
            },
            {
                'name': 'max_weekly_hours'
            },
            {
                'name': 'wage_cents'
            },
            {
                'name': 'wage_type'
            },
            {
                'name': 'wages'
            },
            {
                'name': 'permissions_template_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{identifier}-DELETE': {
        'parameters': [
            {
                'name': 'inactive_reason'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'inactive_comments'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users/{identifier}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/users-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'location_id'
            },
            {
                'name': 'department_id'
            },
            {
                'name': 'role_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/users/{identifier}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'preferred_first_name'
            },
            {
                'name': 'preferred_last_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'mobile_number'
            },
            {
                'name': 'home_number'
            },
            {
                'name': 'address'
            },
            {
                'name': 'postal_zip'
            },
            {
                'name': 'city'
            },
            {
                'name': 'prov_state'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'hire_date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'punch_id'
            },
            {
                'name': 'birth_date'
            },
            {
                'name': 'language'
            },
            {
                'name': 'appear_as_employee'
            },
            {
                'name': 'subscribe_to_updates'
            },
            {
                'name': 'max_weekly_hours'
            },
            {
                'name': 'active'
            },
            {
                'name': 'pronouns'
            },
            {
                'name': 'permissions_template_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/webhooks-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'method'
            },
            {
                'name': 'event'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/webhooks/{webhook_id}-DELETE': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'webhook_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
    '/v2/company/{company_id}/test_webhook-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/v2/company/{company_id}/webhooks-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/company/{company_id}/webhooks/{webhook_id}-PUT': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'webhook_id'
            },
            {
                'name': 'x-api-version'
            },
            {
                'name': 'x-company-guid'
            },
        ]
    },
};