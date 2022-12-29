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
 * @interface PodcastEpisodeSearchResultOut
 */
export interface PodcastEpisodeSearchResultOut {
    /**
     * 
     * @type {number}
     * @memberof PodcastEpisodeSearchResultOut
     */
    id: number;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    podcastName: string;
    /**
     * 
     * @type {PodcastOut}
     * @memberof PodcastEpisodeSearchResultOut
     */
    podcast: PodcastOut;
    /**
     * 
     * @type {Date}
     * @memberof PodcastEpisodeSearchResultOut
     */
    date: Date;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    title: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    description: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    resolvedAudioUrl: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    detailsUrl: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    slug: string;
    /**
     * 
     * @type {number}
     * @memberof PodcastEpisodeSearchResultOut
     */
    duration: number;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeSearchResultOut
     */
    headline: string;
}

/**
 * Check if a given object implements the PodcastEpisodeSearchResultOut interface.
 */
export function instanceOfPodcastEpisodeSearchResultOut(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "id" in value;
    isInstance = isInstance && "podcastName" in value;
    isInstance = isInstance && "podcast" in value;
    isInstance = isInstance && "date" in value;
    isInstance = isInstance && "title" in value;
    isInstance = isInstance && "description" in value;
    isInstance = isInstance && "resolvedAudioUrl" in value;
    isInstance = isInstance && "detailsUrl" in value;
    isInstance = isInstance && "slug" in value;
    isInstance = isInstance && "duration" in value;
    isInstance = isInstance && "headline" in value;

    return isInstance;
}

export function PodcastEpisodeSearchResultOutFromJSON(json: any): PodcastEpisodeSearchResultOut {
    return PodcastEpisodeSearchResultOutFromJSONTyped(json, false);
}

export function PodcastEpisodeSearchResultOutFromJSONTyped(json: any, ignoreDiscriminator: boolean): PodcastEpisodeSearchResultOut {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'podcastName': json['podcast_name'],
        'podcast': PodcastOutFromJSON(json['podcast']),
        'date': (new Date(json['date'])),
        'title': json['title'],
        'description': json['description'],
        'resolvedAudioUrl': json['resolved_audio_url'],
        'detailsUrl': json['details_url'],
        'slug': json['slug'],
        'duration': json['duration'],
        'headline': json['headline'],
    };
}

export function PodcastEpisodeSearchResultOutToJSON(value?: PodcastEpisodeSearchResultOut | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'podcast_name': value.podcastName,
        'podcast': PodcastOutToJSON(value.podcast),
        'date': (value.date.toISOString().substr(0,10)),
        'title': value.title,
        'description': value.description,
        'resolved_audio_url': value.resolvedAudioUrl,
        'details_url': value.detailsUrl,
        'slug': value.slug,
        'duration': value.duration,
        'headline': value.headline,
    };
}

