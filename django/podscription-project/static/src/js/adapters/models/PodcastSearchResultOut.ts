/* tslint:disable */
/* eslint-disable */
/**
 * NinjaAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { PodcastOut } from './PodcastOut';
import {
    PodcastOutFromJSON,
    PodcastOutFromJSONTyped,
    PodcastOutToJSON,
} from './PodcastOut';

/**
 * 
 * @export
 * @interface PodcastSearchResultOut
 */
export interface PodcastSearchResultOut {
    /**
     * 
     * @type {number}
     * @memberof PodcastSearchResultOut
     */
    episodeId: number;
    /**
     * 
     * @type {PodcastOut}
     * @memberof PodcastSearchResultOut
     */
    podcast: PodcastOut;
    /**
     * 
     * @type {string}
     * @memberof PodcastSearchResultOut
     */
    headline: string;
}

/**
 * Check if a given object implements the PodcastSearchResultOut interface.
 */
export function instanceOfPodcastSearchResultOut(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "episodeId" in value;
    isInstance = isInstance && "podcast" in value;
    isInstance = isInstance && "headline" in value;

    return isInstance;
}

export function PodcastSearchResultOutFromJSON(json: any): PodcastSearchResultOut {
    return PodcastSearchResultOutFromJSONTyped(json, false);
}

export function PodcastSearchResultOutFromJSONTyped(json: any, ignoreDiscriminator: boolean): PodcastSearchResultOut {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'episodeId': json['episode_id'],
        'podcast': PodcastOutFromJSON(json['podcast']),
        'headline': json['headline'],
    };
}

export function PodcastSearchResultOutToJSON(value?: PodcastSearchResultOut | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'episode_id': value.episodeId,
        'podcast': PodcastOutToJSON(value.podcast),
        'headline': value.headline,
    };
}

